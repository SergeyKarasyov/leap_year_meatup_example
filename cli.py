#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" a command line interface to the python tool for leap year check
"""

import click  # pylint: disable=import-error

from is_leap import is_leap
from logger import LOGGER


@click.group()
def cli() -> None:
    """ part of cli implementation via click"""
    pass


@cli.command("is_leap")
@click.option("--year", help="the year to check", nargs=1, required=True, type=(int))
def is_leap_cli(year: int) -> None:
    """function to call the is_leap module
    """
    LOGGER.info("is_leap_cli({}) is {}".format(year, is_leap(year)))


if __name__ == "__main__":
    cli()
