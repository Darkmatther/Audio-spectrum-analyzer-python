from ffmpy import FFmpeg
import pyaudio
import wave
import os
import sys
import struct
import math
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.interpolate import spline


class AudioSpectrum():
    """Audio frequency spectrum object"""

    def __init__(self, input, CHUNK = 1024):

        self._input = input #Input audio file
        self._CHUNK = CHUNK #Integration window for spectrum calculation (number of measurements)
        
        self.compute(self._input)

        self.printInfo()


    def compute(self, input):
        """Compute audio spectrum"""

        #Convert file to .wav
        file = convertAudio(input, '.wav')

        #Open .wav file
        wf = wave.open(file, 'rb')

        #Get sampling rate
        rate = wf.getframerate()

        #Get frequency values
        freq = [k * rate/self._CHUNK for k in range(0, self._CHUNK)]

        #Instantiate PyAudio
        p = pyaudio.PyAudio()    

        #Define list of times values and spectrum measurements
        spectrum = []
        time = []
        count = 0

        #Read data (chunk by chunk)
        data = wf.readframes(self._CHUNK)
        while len(data) == 4*self._CHUNK:

            #Fill in time value
            count += 1
            time.append(count * self._CHUNK / rate)

            #Convert to human-readable data
            data_int = struct.unpack(str(4*self._CHUNK) + 'B', data) #Get raw waveform data

            #Compute FFT
            data_fft = fft(data_int)

            #Get spectrum data from FFT
            data_spectrum = np.abs(data_fft[0:self._CHUNK]) / (128 * self._CHUNK)

            #Fill in spectrum data
            spectrum.append(data_spectrum)

            #Read next chunk of data
            data = wf.readframes(self._CHUNK)

        #Close PyAudio
        p.terminate()

        #Set class attributes
        self._RATE = rate
        self._time = np.array(time)
        self._freq = np.array(freq)
        self._spectrum = np.array(spectrum)


    def showSpectrum(self, sec):
        """Plot frequency spectrum of the audio file at a given time (in seconds)"""

        #Get self._time value closest to sec
        n = 1
        for i, t in enumerate(self._time[1:]):
            if t >= sec:
                break
            n = i

        #Get raw spectrum
        spectrum = self._spectrum[n]

        #Get spectrum in decibel (dB)
        spectrum_db = np.apply_along_axis(np.vectorize(self.convertToDecibels), 0, spectrum, spectrum[0]) #Spectrum[0] represents the reference amplitude for the dB conversion

        #Get smooth spectrum values on the whole frequency range (do not account for freq = 0)
        freq_smooth = np.logspace(math.log10(self._freq[1:].min()), math.log10(self._freq[1:].max()), self._CHUNK)
        spectrum_db_smooth = spline(self._freq[1:], spectrum_db[1:], freq_smooth)
        
        #Plot spectrum (x = frequency in log scale, y = amplitude)
        plt.figure(figsize = (15, 3))
        plt.subplots_adjust(top = 0.90, bottom = 0.20, left = 0.05, right = 0.95, hspace = 0.50, wspace = 0.00)
        plt.plot(freq_smooth, spectrum_db_smooth, 'k', linewidth = 1.0)
        plt.title(r"Audio spectrum at t = " + str(sec) + "s")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude (dB)")
        plt.xlim(20, 20000)
        plt.ylim(-100, 0)
        plt.xscale('log')
        plt.grid(True)

        plt.draw()
        #plt.show()

        #Return raw spectrum data at time n
        return self._spectrum[n], self._time[n], n

    
    def convertToDecibels(self, a, amp_ref):
        """Convert FFT amplitude into decibels"""

        if a < 1.0e-30: 
            return -600
        else: 
            return 20 * math.log10(a / amp_ref)


    def printInfo(self):
        """Print basic information about the audio spectrum"""

        print('CHUNK = ', self._CHUNK)
        print('RATE = ', self._RATE, 'Hz')
        print('Times = ', self._time, ' (seconds)')
        print('Frequencies = ', self._freq, ' (Hz)')
        print('Spectrum = ', self._spectrum.shape)



def convertAudio(file, output_extension = '.wav'):
    """Convert input audio file into another format"""

    name, ext = os.path.splitext(file)

    if ext != output_extension:
        outFile = name + output_extension
        ff = FFmpeg(
            inputs={file: None},
            outputs={outFile: None},
            global_options = "-y"
        )
        ff.cmd
        ff.run()
        return outFile

    else:
        return file



#Test with audio file
spectrum = AudioSpectrum('audio_test.wav')
spectrum.showSpectrum(25)
spectrum.showSpectrum(200)
spectrum.showSpectrum(300)

plt.show()

