# -*- coding: utf-8 -*-
#
# This file is part of the SKAPowerSupply project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" Power Supply for the SKA Project

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
from skabase.SKABaseDevice import SKABaseDevice
# Additional import
# PROTECTED REGION ID(SKAPowerSupply.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  SKAPowerSupply.additionnal_import

__all__ = ["SKAPowerSupply", "main"]


class SKAPowerSupply(SKABaseDevice):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(SKAPowerSupply.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SKAPowerSupply.class_variable

    # -----------------
    # Device Properties
    # -----------------





    # ----------
    # Attributes
    # ----------









    Voltage = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
    )

    Current = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )


    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKABaseDevice.init_device(self)
        # PROTECTED REGION ID(SKAPowerSupply.init_device) ENABLED START #
        # PROTECTED REGION END #    //  SKAPowerSupply.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(SKAPowerSupply.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKAPowerSupply.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(SKAPowerSupply.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKAPowerSupply.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Voltage(self):
        # PROTECTED REGION ID(SKAPowerSupply.Voltage_read) ENABLED START #
        return 0.0
        # PROTECTED REGION END #    //  SKAPowerSupply.Voltage_read

    def write_Voltage(self, value):
        # PROTECTED REGION ID(SKAPowerSupply.Voltage_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKAPowerSupply.Voltage_write

    def write_Current(self, value):
        # PROTECTED REGION ID(SKAPowerSupply.Current_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  SKAPowerSupply.Current_write


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(SKAPowerSupply.main) ENABLED START #
    return run((SKAPowerSupply,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SKAPowerSupply.main

if __name__ == '__main__':
    main()
