#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile
from tools.command_parser import CommandParser
from tools.fourier_transformation import dft
from tools.model import Model


class Analyzer:
    def __init__(self, sampling_frequency: int, frame_length: int, overlap: int, pre_emphasis: float):
        self.sampling_frequency = sampling_frequency
        self.frame_length = frame_length
        self.overlap = overlap
        self.hop = self.frame_length - self.overlap
        self.pre_emphasis = pre_emphasis

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
        emphasized_signal = np.append(normalized_file_samples[0], normalized_file_samples[1:] - self.pre_emphasis * normalized_file_samples[:-1])

        # Split audio signal to frames
        frames = list()
        for f in range(int((len(emphasized_signal) - self.frame_length)/self.hop)):
            frames.append(emphasized_signal[f*self.hop:f*self.hop+self.frame_length])  # TODO: Add Hamming window
        
        # Compute absolute value of dft of every frame
        dft_frames = list()
        for frame in frames:
            dft_frames.append(np.abs(dft(frame)))

        # Return model
        model = Model()
        model.frame_energies = dft_frames
        return model
