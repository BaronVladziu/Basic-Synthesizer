#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
from tools.autocorrelation import calculate_autocorrelation
from tools.command_parser import CommandParser
from tools.filtration import BandFilter
from tools.fourier_transformation import fft
from tools.model import Model, Frame


class Analyzer:
    def __init__(self, sampling_frequency: int, frame_length: int, overlap: int, pre_emphasis: float):
        self.sampling_frequency = sampling_frequency
        self.frame_length = frame_length
        self.overlap = overlap
        self.hop = self.frame_length - self.overlap
        self.pre_emphasis = pre_emphasis
        self.hamming_window = 0.54 - 0.46*np.cos((2*np.pi*np.arange(self.frame_length))/(self.frame_length - 1))

    def analyze(self, command: str) -> Model:
        print('Analyzing command "' + command + '"...')

        # Load audio file
        sampling_frequency, file_samples = scipy.io.wavfile.read('audio-files/' + command + '.wav')
        if sampling_frequency != self.sampling_frequency:
            raise ValueError('Sampling frequency does not match' +\
                             'sampling frequency of analyzed audio files!')
        if len(np.shape(file_samples)) > 1:
            raise ValueError('Only mono audio files are supported!')

        # Remove mean value
        normalized_file_samples = file_samples - np.mean(file_samples)

        # Pre-emphasis
        # emphasized_signal = np.append(normalized_file_samples[0], normalized_file_samples[1:] - self.pre_emphasis * normalized_file_samples[:-1])
        emphasized_signal = normalized_file_samples

        # Split audio signal to frames multiplied by hamming window
        frames = list()
        for f in range(int((len(emphasized_signal) - self.frame_length)/self.hop)):
            frames.append(emphasized_signal[f*self.hop:f*self.hop+self.frame_length]*self.hamming_window)

        # Compute absolute value of dft of every frame
        dft_frames = list()
        for frame in frames:
            dft_frames.append(np.abs(fft(frame)))

        # Compute base frequency of every frame
        band_filter = BandFilter(start_frequency=0, stop_frequency=200, sampling_frequency=self.sampling_frequency, order=8)
        base_frequencies = list()
        for frame in frames:
            # Calculate autocorrelation signal
            autocorrelation_signal = calculate_autocorrelation(frame)

            # Find highest value index (above 60Hz and below 200Hz)
            last_sample_id = int(self.sampling_frequency/60) + 1
            first_sample_id = int(self.sampling_frequency/200)
            peak_index = first_sample_id + np.argmax(autocorrelation_signal[first_sample_id:last_sample_id])
            peak_value = autocorrelation_signal[peak_index]

            if peak_value >= 0.4:
                # Use harmonic pulse generator
                base_frequencies.append(self.sampling_frequency/peak_index)

            else:
                # Use white noise generator
                base_frequencies.append(0)
        
        plt.plot(base_frequencies)
        plt.show()

        # Return model
        model = Model()
        for i in range(len(dft_frames)):
            frame = Frame(energies=dft_frames[i], base_frequency=base_frequencies[i])
            model.frames.append(frame)
        return model
