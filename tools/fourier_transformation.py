#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def dft(x: np.array) -> np.array:
    n = len(x)
    y = np.zeros(n, dtype=np.complex_)
    for k in range(n):
        for t in range(n):
            y[k] += x[t]*np.exp(-2j*np.pi*t*k/n)
    return y


def idft(y: np.array) -> np.array:
    n = len(y)
    x = np.zeros(n, dtype=np.complex_)
    for t in range(n):
        for k in range(n):
            x[t] += y[k]*np.exp(2j*np.pi*t*k/n)
    return x/n


def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("Size of x must be a power of 2")

    # N_min here is equivalent to the stopping condition above,
    # and should be a power of 2
    N_min = min(N, 32)

    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        x_even = X[:, :int(X.shape[1] / 2)]
        x_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0]) / X.shape[0])[:, None]
        X = np.vstack([x_even + factor * x_odd, x_even - factor * x_odd])

    return X.ravel()
