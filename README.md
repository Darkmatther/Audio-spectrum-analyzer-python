# Audio spectrum analyzer in python

## Description
This python program takes an audio input file as an input and returns an AudioSpectrum object that consists of the frequency spectrum of the audio at different times, in easy-to-manipulate numpy arrays.

## AudioSpectrum object
The spectrum is stored in an AudioSpectrum objet, as well as several other attributes :
_input : the input audio file in original format
_CHUNK : the number of audio amplitude measurements that are used for FFT calculation. By default is is 1024 (should be a power of 2)
_RATE : the original sampling rate of the input audio file

_time : the list of times associated with each spectrum measurement
_freq : the list of frequencies resulting from the FFT
_spectrum : the frequency spectrum of the audio file as a 2D numpy array

Example: 

## Example with test audio file, at t = 25s

Note: the audio file is first converted into .wav format using FFMPEG library so that I can use the wave python library to access the audio data

## Useful links
http://claude.lahache.free.fr/lenumerique/analyse-spectrale-par-fft.pdf
https://www.unilim.fr/pages_perso/jean.debord/math/fourier/fft.htm
https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fft.html
