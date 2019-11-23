#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def dft(x: np.array) -> np.array:
    n = len(x)
    y = np.zeros(n)
    for k in range(n):
        for t in range(n):
            y[k] += x[t]*np.exp(-2j*np.pi*t*k/n)
    return y


def idft(y: np.array) -> np.array:
    n = len(y)
    x = np.zeros(n)
    for t in range(n):
        for k in range(n):
            x[t] += y[k]*np.exp(2j*np.pi*t*k/n)
    return x/n
