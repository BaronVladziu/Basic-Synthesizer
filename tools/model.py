#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Frame:
    def __init__(self, energies, base_frequency):
        self.energies = energies
        self.base_frequency = base_frequency

    def get_frame_length(self):
        return len(self.energies)


class Model:
    def __init__(self):
        self.frames = list()

    def get_frame_length(self):
        if len(self.frames) <= 0:
            raise ValueError('Model has no frames, so it cannot calculate frame length!')
        return self.frames[0].get_frame_length()
