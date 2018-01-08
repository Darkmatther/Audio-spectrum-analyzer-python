# Audio spectrum analyzer in python

![Audio spectrum - example](https://user-images.githubusercontent.com/25090342/34655930-26b1ec96-f412-11e7-8732-98b0218a0768.png "Audio spectrum - example")

## Description
This python program takes an audio file as an input and returns an AudioSpectrum object that consists of the frequency spectrum of the audio at different times, in easy-to-manipulate numpy arrays.<br>

Note: the audio file is first converted into .wav format using *FFMPEG* library so that I can use the *wave* python library to access the audio data and read it chunk by chunk (1 chunk <-> 1 spectrum measurement)

## AudioSpectrum class
The spectrum of the audio file is stored in an AudioSpectrum objet, which contains several attributes :
<br>
- _input : the input audio file in its original format<br>
- _CHUNK : the number of audio waveform measurements that are used for FFT calculation.<br>
By default is is 1024 (should be a power of 2)<br>
- _RATE : the original sampling rate of the input audio file<br>
(i.e. number of audio waveform measurements per second, often 44100 Hz)
<br><br>
- **_spectrum** : the frequency spectrum of the audio file as a 2D numpy array<br>
- **_time** : the list of times associated with each spectrum measurement (in seconds)<br>
- **_freq** : the list of frequencies in the spectrum (in Hz)<br>
<br>
Notes:<br>
_spectrum.shape = (len(_time), len(_freq))<br>
_spectrum[i] is the ith measurement of the audio spectrum, corresponding to the audio chunk that finishes at time = _time[i]<br>
_spectrum[i][j] is the amplitude of the spectrum for frequency _freq[j] at time _time[i]<br>
<br>
The audio spectrum of a file can be very useful when applied to music projects, and/or as a preprocessing step for machine learning/deep learning applications

## Example with test audio file
The *showSpectrum(self, sec)* method can be used to plot the audio spectrum at time *sec*. Here is an example with an audio test file at t = 25s :
![Audio spectrum - example](https://user-images.githubusercontent.com/25090342/34655930-26b1ec96-f412-11e7-8732-98b0218a0768.png "Audio spectrum - example")

## Useful links
http://claude.lahache.free.fr/lenumerique/analyse-spectrale-par-fft.pdf<br>
https://www.unilim.fr/pages_perso/jean.debord/math/fourier/fft.htm<br>
https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fft.html
