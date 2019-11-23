#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


class BaseSignalGenerator:
    def __init__(self, sampling_frequency: int):
        self.sampling_frequency = sampling_frequency

    def generate_base_signal(length: int, frequency: float) -> np.array:
        if frequency == 0:
            # Generate white noise
            return np.random.rand(length)
        else:
            # Generate repeating impulse signal
            generated_signal = np.zeros(length)
            for i in np.arange(0, length, 1/self.sampling_frequency):
                if i > 1/frequency:
                    generated_signal[int(i)] = 1
            return generated_signal
