#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class BaseSignalGenerator:
    def __init__(self, sampling_frequency: int):
        self.sampling_frequency = sampling_frequency

    def generate_pulses(self, length: int, frequency: float) -> np.array:
        # Generate repeating impulse signal
        generated_signal = np.zeros(length)
        for i in np.arange(0, length, 1/self.sampling_frequency):
            if i > 1/frequency:
                generated_signal[int(i)] = 1
        return generated_signal

    def generate_white_noise(self, length: int) -> np.array:
        # Generate white noise
        return np.random.rand(length)
