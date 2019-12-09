#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from analysis.analyzer import Analyzer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
from synthesis.base_signal_generator import BaseSignalGenerator
from tools.command_parser import CommandParser
from tools.fourier_transformation import fft, idft


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

        # Create base signal generator
        print('Synthesizing command "' + parsed_command + '"...')
        base_signal_generator = BaseSignalGenerator(self.sampling_frequency)

        # Synthesize all frames (generate base signal + filter)
        dft_frames = list()
        for frame in model.frames:
            if frame.base_frequency == 0:
                base_signal = base_signal_generator.generate_white_noise(model.get_frame_length())
            else:
                base_signal = base_signal_generator.generate_pulses(model.get_frame_length(), frame.base_frequency)
            base_signal_dft = fft(base_signal)
            dft_frames.append(base_signal_dft*frame.energies)

        # Merge all frames using overlap-add technique
        synthesized_signal = np.array(np.real(idft(dft_frames[0])) * analyzer.hamming_window)
        window_signal = analyzer.hamming_window
        for i in range(1, len(dft_frames)):
            synthesized_signal = np.concatenate([synthesized_signal, np.zeros(self.hop)])
            window_signal = np.concatenate([window_signal, np.zeros(self.hop)])
            synthesized_signal[i*self.hop:i*self.hop+self.frame_length] += np.real(idft(dft_frames[i])) * analyzer.hamming_window
            window_signal[i*self.hop:i*self.hop+self.frame_length] += analyzer.hamming_window

        # Make sure not to divide by zero
        for i in range(len(window_signal)):
            if 0.1 > window_signal[i] > -0.1:
                if window_signal[i] >= 0:
                    window_signal[i] = 0.1
                else:
                    window_signal[i] = -0.1

        # Divide signal by windows to remove buzzing
        synthesized_signal = synthesized_signal/window_signal

        # Normalize signal
        synthesized_signal /= np.max(synthesized_signal)

        # Plot and save to file
        plt.plot(synthesized_signal)
        plt.show()
        scipy.io.wavfile.write('output.wav', self.sampling_frequency, synthesized_signal)
