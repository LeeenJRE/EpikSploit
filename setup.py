#!/usr/bin/env python
import os
from setuptools import setup

data = {'': ["VERSION.TXT"]}
for folder in ["banner", "commands", "modules"]:
    for root, __, files in os.walk(os.path.join("epiksploit", "_src", folder)):
        _, root = root.split(os.path.sep, 1)
        for f in files:
            data[''].append(os.path.join(root, f))

setup(package_data=data)