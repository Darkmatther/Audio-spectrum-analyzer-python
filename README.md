# Audio spectrum analyzer in python

## Description
This python program takes an audio input file as an input and returns an AudioSpectrum object that consists of the frequency spectrum of the audio at different times, in easy-to-manipulate numpy arrays.

Note: the audio file is first converted into .wav format using FFMPEG library so that I can use the wave python library to access the audio data

## AudioSpectrum object
The spectrum of the audio file is stored in an AudioSpectrum objet, which also contains other attributes :
<br>
_input : the input audio file in its original format<br>
_CHUNK : the number of audio waveform measurements that are used for FFT calculation. By default is is 1024 (should be a power of 2)<br>
_RATE : the original sampling rate of the input audio file (i.e. number of audio waveform measurements per second, often 44100 Hz)
<br><br>
_spectrum : the frequency spectrum of the audio file as a 2D numpy array<br>
_time : the list of times associated with each spectrum measurement (in seconds)<br>
_freq : the list of frequencies in the spectrum (in Hz)<br>
<br>
Note: 
_spectrum.shape = (len(_time), len(_freq))
_spectrum[i] is the ith measurement of the audio spectrum, corresponding to time _time[i]
_spectrum[i][j] is the amplitude of the spectrum for frequency _freq[j] in the ith measurement of the spectrum

## Example with test audio file



## Useful links
http://claude.lahache.free.fr/lenumerique/analyse-spectrale-par-fft.pdf
https://www.unilim.fr/pages_perso/jean.debord/math/fourier/fft.htm
https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fft.html
