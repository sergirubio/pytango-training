# -*- coding: utf-8 -*-
#
# This file is part of the FixedCurrentPowerSupply project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" FixedCurrentPowerSupply

A dummy power supply for testing
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run

from FixedCurrentPowerSupply import FixedCurrentPowerSupply
from SKAPowerSupply import SKAPowerSupply

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(FixedCurrentPowerSupply.main) ENABLED START #
    return run((FixedCurrentPowerSupply,SKAPowerSupply), args=args, **kwargs)
    # PROTECTED REGION END #    //  FixedCurrentPowerSupply.main

if __name__ == '__main__':
    main()
