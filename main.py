#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from synthesis.synthesizer import Synthesizer


def main(command: str) -> None:
    synthesizer = Synthesizer()
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
    args = parser.parse_args()

    main(args.command)
