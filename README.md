# Basic Speech Synthesizer

This project is a very simple parametric speech synthesizer.

## Features:

It's (will be) capable of synthesizing following words (all are in Polish language):

1) Poniedziałek (Monday)
2) Wtorek (Tuesday)
3) Środa (Wednesday)
4) Czwartek (Thursday)
5) Piątek (Friday)
6) Sobota (Saturday)
7) Niedziela (Sunday)

8) Wiosna (Spring)
9) Lato (Summer)
10) Jesień (Autumn)
11) Zima (Winter)

## Requirements:

- Python 3.6+

## Usage:

To start synthesizer run `main.py` script.

You will be able to write command for synthesis then.

You can use polish or english word and numeric identifier,
but all will result in the same audio file.

Example:
All following commands
```
Lato
Summer
9
```
result in audio file with the word "Sobota" inside.

Synthesized audio is played when synthesized and
saved as an `.wav` file in the main directory.
