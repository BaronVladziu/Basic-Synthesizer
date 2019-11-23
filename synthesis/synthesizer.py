#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from synthesis.base_signal_generator import BaseSignalGenerator
from synthesis.command_parser import CommandParser


class Synthesizer:
    def __init__(self, sampling_frequency: int):
        self.sampling_frequency = sampling_frequency

    def synthesize(self, command: str) -> None:
        print('Synthesizing command "' + command + '"...')

        command_parser = CommandParser()
        parsed_command = command_parser.parse_command(command)

        # Choose model of given word
        raise NotImplementedError("To be implemented")

        # Synthesize all frames (generated base signal + filter)
        base_signal_generator = BaseSignalGenerator(self.sampling_frequency)
        raise NotImplementedError("To be implemented")

        # Merge all frames using overlap-add technique
        raise NotImplementedError("To be implemented")

        # Save to file
        raise NotImplementedError("To be implemented")
