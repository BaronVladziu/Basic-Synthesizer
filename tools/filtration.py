#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from tools.fourier_transformation import fft, idft


class BandFilter:
    def __init__(self, start_frequency: float, stop_frequency: float, sampling_frequency: int, order: int):
        self.start_frequency = start_frequency
        self.stop_frequency = stop_frequency
        self.sampling_frequency = sampling_frequency

        # Check argument correctness
        if start_frequency < 0 or stop_frequency < 0 or sampling_frequency < 0:
            raise ValueError('All frequencies must be higher or equal to zero!')
        if start_frequency >= stop_frequency:
            raise ValueError('Start frequency of the band filter must be lower than stop frequency!')
        if start_frequency >= sampling_frequency/2:
            raise ValueError('Start frequency of the band filter must be lower than nyquist frequency!')
        if stop_frequency >= sampling_frequency/2:
            raise ValueError('Stop frequency of the band filter must be lower than nyquist frequency!')
        if order < 2:
            raise ValueError('Band filter order must be at least 2!')
        
        # Create dft filter of given order
        self.dft_signal = np.zeros(order)
        for i in range(int(order/2)+1):
            if start_frequency/sampling_frequency <= i/order < stop_frequency/sampling_frequency:
                self.dft_signal[i] = 1
                self.dft_signal[-i] = 1
        
        # Calculate impulse response
        self.impulse_response = np.real(idft(self.dft_signal))

    def filter(self, signal: np.array, cut_to_input_length=True) -> np.array:
        output = np.zeros(len(signal) + len(self.impulse_response) - 1)
        for l in range(len(output)):
            for n in range(len(signal)):
                if 0 <= l-n < len(self.impulse_response):
                    output[l] += signal[n]*self.impulse_response[l-n]
        if cut_to_input_length:
            output = output[len(self.impulse_response) - 1:]
        return output
