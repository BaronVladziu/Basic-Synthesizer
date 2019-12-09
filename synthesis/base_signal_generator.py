#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class BaseSignalGenerator:
    def __init__(self, sampling_frequency: int):
        self.sampling_frequency = sampling_frequency
        self.phase = 0

    def generate_pulses(self, length: int, frequency: float) -> np.array:
        # Generate repeating impulse signal
        generated_signal = np.zeros(length)
        for i in range(length):
            self.phase += 2*np.pi*frequency/self.sampling_frequency
            while self.phase > 2*np.pi:
                generated_signal[i] = 1
                self.phase -= 2 * np.pi
        return generated_signal

    def generate_white_noise(self, length: int) -> np.array:
        # Generate white noise
        return np.random.rand(length)
