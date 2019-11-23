#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from command_parser import CommandParser


class Synthesizer:
    def synthesize(self, command: str) -> None:
        print('Synthesizing command "' + command + '"...')

        command_parser = CommandParser()
        parsed_command = command_parser.parse_command(command)

        # Choose model of given word
        raise NotImplementedError("To be implemented")

        # Synthesize all frames (generated base signal + filter)
            raise NotImplementedError("To be implemented")

        # Merge all frames using overlap-add technique
            raise NotImplementedError("To be implemented")

        # Save to file
            raise NotImplementedError("To be implemented")
