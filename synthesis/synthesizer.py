#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analysis.analyzer import Analyzer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
from synthesis.base_signal_generator import BaseSignalGenerator
from tools.command_parser import CommandParser
from tools.fourier_transformation import dft, idft


class Synthesizer:
    def __init__(self, sampling_frequency: int):
        self.sampling_frequency = sampling_frequency
        self.frame_length = 256
        self.overlap = int(0.25*self.frame_length)
        self.hop = self.frame_length - self.overlap
        self.pre_emphasis = 0.97

    def synthesize(self, command: str) -> None:
        # Parse command
        command_parser = CommandParser()
        parsed_command = command_parser.parse_command(command)

        # Create model of given word
        analyzer = Analyzer(self.sampling_frequency, self.frame_length, self.overlap, self.pre_emphasis)
        model = analyzer.analyze(parsed_command)

        # Create base signal
        print('Synthesizing command "' + parsed_command + '"...')
        base_signal_generator = BaseSignalGenerator(self.sampling_frequency)
        base_signal = base_signal_generator.generate_white_noise(model.get_frame_length())
        base_signal_dft = dft(base_signal)

        # Synthesize all frames (generated base signal + filter)
        dft_frames = list()
        for energies in model.frame_energies:
            dft_frames.append(base_signal_dft*energies)

        # Merge all frames using overlap-add technique  # TODO: Add Hamming window
        synthesized_signal = np.array(np.real(idft(dft_frames[0])))
        for i in range(1, len(dft_frames)):
            synthesized_signal = np.concatenate([synthesized_signal, np.zeros(self.hop)])
            synthesized_signal[i*self.hop:i*self.hop+self.frame_length] += np.real(idft(dft_frames[i]))

        # Normalize signal
        synthesized_signal /= np.max(synthesized_signal)

        # Save to file
        plt.plot(synthesized_signal)
        plt.show()
        scipy.io.wavfile.write('output.wav', self.sampling_frequency, synthesized_signal)
