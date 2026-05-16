#!/usr/bin/env python3

from subprocess import run, CompletedProcess, CalledProcessError
from argparse import ArgumentParser
from sys import exit
from juno import juno
from termcolor import colored

USB_path: str = "/dev/ttyUSB"

_flag = [
    colored(" " * 22, (91, 206, 250), (91, 206, 250)),
    colored(" " * 22, (245, 169, 184), (245, 169, 184)),
    colored(" " * 22, (255, 255, 255), (255, 255, 255)),
    colored(" " * 22, (245, 169, 184), (245, 169, 184)),
    colored(" " * 22, (91, 206, 250), (91, 206, 250)),
]


def _change_usb_perms(USB: int) -> bool:
    """Changes the permisions of the USB ports.

    Args:
        USB: The ID of the usb port e.g. 0 or 1.

    Returns:
        bool: If the permisions were updated successfully.
    """
    try:
        usb: CompletedProcess[bytes] = run(
            f"sudo chmod 666 {USB_path}{USB}", shell=True, check=True
        )

        if usb.check_returncode():
            return True

        return False

    except CalledProcessError | Exception as e:
        print("ERROR[Changing port perms]: ", e)
        return False


if __name__ == "__main__":
    try:
        usage: str = f"""
Juno Serial application

A small python applciation designed to enable connecting to a Arm Juno
development boards over a serial connection and update it's firmware over USB.

By: Lily Wilks

{_flag[0]}
{_flag[1]}
{_flag[2]}
{_flag[3]}
{_flag[4]}
"""

        cli: ArgumentParser = ArgumentParser(
            prog="Juno Serial",
            usage=usage,
        )

        cli.add_argument(
            "--usb0", action="store_true", help="Connect to serial connection USB0."
        )

        cli.add_argument(
            "--usb1", action="store_true", help="Connect to serial connection USB1."
        )

        cli.add_argument(
            "--usb", action="store_true", help="Enable the Juno's USB port"
        )

        cli.add_argument(
            "--lsp",
            action="store_true",
            help="Lists out all available serial connections.",
        )

        args = cli.parse_args()

        if args.usb0:
            _change_usb_perms(0)
            juno(USB=0).open_serial()
            exit(0)

        if args.usb1:
            _change_usb_perms(1)
            juno(USB=1).open_serial()

        if args.usb:
            print("WORK IN PROGRESS")
            exit(0)

        if args.lsp:
            print("WORK IN PROGRESS")
            exit(0)

    except Exception as e:
        print("ERROR[main process]: ", e)
        exit(1)
