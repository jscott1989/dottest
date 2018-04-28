#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="dotTest",
      version="0.1",
      description="Set up .test domains for local development",
      packages=find_packages(),
      scripts=["dottest"],
      install_requires=[
        "docopt>=0.6.2",
        "sh>=1.12.14"
      ]
      )
