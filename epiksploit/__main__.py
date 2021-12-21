#!/usr/bin/python3
# -*- coding: utf-8 -*-
from epiksploit.__info__ import __author__, __copyright__, __email__, __license__, __version__
from epiksploit import EpikSploitConsole
from tinyscript import *

__name__ = "__main__"
__script__ = "epiksploit"
__doc__    = """
EpikSploit framework.
"""

def at_exit():
    subprocess.call("service network-manager restart", shell=True)
    if not args.dev:
        subprocess.call("reset", shell=True)


def main():
    parser.add_argument("--dev", action="store_true", help="development mode")
    initialize(exit_at_interrupt=False, sudo=True)
    c = EpikSploitConsole(
        __scriptname__,
        banner_section_styles={'title': {'fgcolor': "lolcat"}},
        dev=args.dev,
        debug=args.verbose,
    )
    c.start()