# -*- coding: UTF-8 -*-
"""EpikSploit package information.

"""
import os

__author__    = "MirageSh"
__email__     = "contact@epiksploit.com"
__copyright__ = "© 2022 EpikSploit"
__license__   = "agpl-3.0"

with open(os.path.join(os.path.dirname(__file__), "VERSION.txt")) as f:
    __version__ = f.read().strip()
