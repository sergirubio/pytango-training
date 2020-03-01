# -*- coding: utf-8 -*-
#
# This file is part of the SKACurrentPowerSupply project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" done

"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
from SKAPowerSupply import SKAPowerSupply
# Additional import
# PROTECTED REGION ID(SKACurrentPowerSupply.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  SKACurrentPowerSupply.additionnal_import

__all__ = ["SKACurrentPowerSupply", "main"]


class SKACurrentPowerSupply(SKAPowerSupply):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(SKACurrentPowerSupply.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SKACurrentPowerSupply.class_variable

    # -----------------
    # Device Properties
    # -----------------





    # ----------
    # Attributes
    # ----------












    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKAPowerSupply.init_device(self)
        # PROTECTED REGION ID(SKACurrentPowerSupply.init_device) ENABLED START #
        # PROTECTED REGION END #    //  SKACurrentPowerSupply.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(SKACurrentPowerSupply.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKACurrentPowerSupply.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(SKACurrentPowerSupply.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKACurrentPowerSupply.delete_device

    # ------------------
    # Attributes methods
    # ------------------


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(SKACurrentPowerSupply.main) ENABLED START #
    return run((SKACurrentPowerSupply,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SKACurrentPowerSupply.main

if __name__ == '__main__':
    main()
