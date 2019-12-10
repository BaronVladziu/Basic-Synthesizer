#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CommandParser:
    def __init__(self):
        self.avaliable_commands = dict()
        self.avaliable_commands['1'] = 'Monday'
        self.avaliable_commands['poniedziałek'] = 'Monday'
        self.avaliable_commands['monday'] = 'Monday'
        self.avaliable_commands['2'] = 'Tuesday'
        self.avaliable_commands['wtorek'] = 'Tuesday'
        self.avaliable_commands['tuesday'] = 'Tuesday'
        self.avaliable_commands['3'] = 'Wednesday'
        self.avaliable_commands['środa'] = 'Wednesday'
        self.avaliable_commands['wednesday'] = 'Wednesday'
        self.avaliable_commands['4'] = 'Thursday'
        self.avaliable_commands['czwartek'] = 'Thursday'
        self.avaliable_commands['thursday'] = 'Thursday'
        self.avaliable_commands['5'] = 'Friday'
        self.avaliable_commands['piątek'] = 'Friday'
        self.avaliable_commands['friday'] = 'Friday'
        self.avaliable_commands['6'] = 'Saturday'
        self.avaliable_commands['sobota'] = 'Saturday'
        self.avaliable_commands['saturday'] = 'Saturday'
        self.avaliable_commands['7'] = 'Sunday'
        self.avaliable_commands['niedziela'] = 'Sunday'
        self.avaliable_commands['sunday'] = 'Sunday'
        self.avaliable_commands['8'] = 'Spring'
        self.avaliable_commands['wiosna'] = 'Spring'
        self.avaliable_commands['spring'] = 'Spring'
        self.avaliable_commands['9'] = 'Summer'
        self.avaliable_commands['lato'] = 'Summer'
        self.avaliable_commands['summer'] = 'Summer'
        self.avaliable_commands['10'] = 'Autumn'
        self.avaliable_commands['jesień'] = 'Autumn'
        self.avaliable_commands['autumn'] = 'Autumn'
        self.avaliable_commands['11'] = 'Winter'
        self.avaliable_commands['zima'] = 'Winter'
        self.avaliable_commands['winter'] = 'Winter'

    def parse_command(self, command: str) -> str:
        command = command.lower()
        if command not in self.avaliable_commands.keys():
            raise ValueError('Unknown synthesis command used!')
        return self.avaliable_commands[command]
