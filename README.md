# Basic Speech Synthesizer

This project is a very simple parametric speech synthesizer.

## Features

It's capable of synthesizing following words (all are in Polish language):

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

## Requirements

- Python 3.6+

## Start

### For windows

To start synthesizer install packages from `requirements.txt` file
and run `main.py` script with synthesis command as argument.

Example:
```shell
python main.py --command "Sobota"
```

### For linux

```shell
./create-venv.sh
./run-synthesizer.sh <synthesis_command>
```

Example:
```shell
./create-venv.sh
./run-synthesizer.sh "Sobota"
```

## Usage

After start you will be able to write command for synthesis.

You can use polish or english word and numeric identifier,
but all will result in the same audio file.

Example:
All following commands
```
Lato
Summer
9
```
result in audio file with the word "Lato" inside.

Synthesized audio saved as an `.wav` file in the `output` directory.

## TODO

- Add pre-emphasis (analyzer.py)
- Add Hamming window (analyzer.py)
- Add Hamming window to OLA method (synthesizer.py)
- Add voiced / unvoiced tracking (analyzer.py + synthesizer.py)
- Add fundamental frequency tracking (analyzer.py + synthesizer.py)
- Add bandwidth filtering instead of simple STFT (analyzer.py + synthesizer.py)
- Use FFT instead of DFT (fourier_transformation.py)
