#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from synthesis.synthesizer import Synthesizer


def main(command: str, sampling_frequency: int) -> None:
    synthesizer = Synthesizer(sampling_frequency)
    synthesizer.synthesize(command)


if __name__ == "__main__":
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument(
        "-c",
        "--command",
        dest="command",
        required=True,
        help="Command for synthesis.",
        type=str
    )
    parser.add_argument(
        "-fs",
        "--sampling_frequency",
        dest="sampling_frequency",
        default=8000,
        help="Sampling frequency of synthesized signal (must match fs of analyzed audio files).",
        type=int
    )
    args = parser.parse_args()

    main(args.command, args.sampling_frequency)
