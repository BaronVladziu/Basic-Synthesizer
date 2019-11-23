#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Model:
    def __init__(self):
        self.frame_energies = None

    def get_frame_length(self):
        if self.frame_energies is None:
            raise ValueError('Model has no frames, so it cannot calculate frame length!')
        return len(self.frame_energies[0])
