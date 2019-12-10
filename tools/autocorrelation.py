#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def calculate_autocorrelation(signal: np.array) -> np.array:
    output = np.zeros(2*len(signal) - 1)
    for l in range(len(output)):
        for n in range(len(signal)):
            if 0 <= n-l < len(signal):
                output[l] += signal[n]*signal[n-l]
    output /= np.max(np.abs(output))
    return output
