#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CommandParser:
    def __init__(self):
        self.avaliable_commands = dict()
        self.avaliable_commands['1'] = 'Monday'
        self.avaliable_commands['Poniedziałek'] = 'Monday'
        self.avaliable_commands['Monday'] = 'Monday'
        self.avaliable_commands['2'] = 'Tuesday'
        self.avaliable_commands['Wtorek'] = 'Tuesday'
        self.avaliable_commands['Tuesday'] = 'Tuesday'
        self.avaliable_commands['3'] = 'Wednesday'
        self.avaliable_commands['Środa'] = 'Wednesday'
        self.avaliable_commands['Wednesday'] = 'Wednesday'
        self.avaliable_commands['4'] = 'Thursday'
        self.avaliable_commands['Czwartek'] = 'Thursday'
        self.avaliable_commands['Thursday'] = 'Thursday'
        self.avaliable_commands['5'] = 'Friday'
        self.avaliable_commands['Piątek'] = 'Friday'
        self.avaliable_commands['Friday'] = 'Friday'
        self.avaliable_commands['6'] = 'Saturday'
        self.avaliable_commands['Sobota'] = 'Saturday'
        self.avaliable_commands['Saturday'] = 'Saturday'
        self.avaliable_commands['7'] = 'Sunday'
        self.avaliable_commands['Niedziela'] = 'Sunday'
        self.avaliable_commands['Sunday'] = 'Sunday'
        self.avaliable_commands['8'] = 'Spring'
        self.avaliable_commands['Wiosna'] = 'Spring'
        self.avaliable_commands['Spring'] = 'Spring'
        self.avaliable_commands['9'] = 'Summer'
        self.avaliable_commands['Lato'] = 'Summer'
        self.avaliable_commands['Summer'] = 'Summer'
        self.avaliable_commands['10'] = 'Autumn'
        self.avaliable_commands['Jesień'] = 'Autumn'
        self.avaliable_commands['Autumn'] = 'Autumn'
        self.avaliable_commands['11'] = 'Winter'
        self.avaliable_commands['Zima'] = 'Winter'
        self.avaliable_commands['Winter'] = 'Winter'

    def parse_command(self, command: str) -> str:
        if command not in self.avaliable_commands.keys():
            raise ValueError('Unknown synthesis command used!')
        return self.avaliable_commands[command]
