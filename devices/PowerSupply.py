# -*- coding: utf-8 -*-
#
# This file is part of the PowerSupply project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" PowerSupply

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
# Additional import
# PROTECTED REGION ID(PowerSupply.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  PowerSupply.additionnal_import

__all__ = ["PowerSupply", "main"]


class PowerSupply(Device):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(PowerSupply.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  PowerSupply.class_variable

    # -----------------
    # Device Properties
    # -----------------

    HWUpdateTime = device_property(
        dtype='double', default_value=1
    )

    LoadImpedance = device_property(
        dtype='double', default_value=0
    )

    # ----------
    # Attributes
    # ----------

    Voltage = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
        max_value=100,
        min_value=-100,
    )

    Current = attribute(
        dtype='double',
        unit="A",
        max_alarm=80,
        min_alarm=-80,
        max_warning=50,
        min_warning=-50,
    )

    LoadImpedance = attribute(
        dtype='double',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(PowerSupply.init_device) ENABLED START #
        # PROTECTED REGION END #    //  PowerSupply.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(PowerSupply.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PowerSupply.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(PowerSupply.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PowerSupply.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Voltage(self):
        # PROTECTED REGION ID(PowerSupply.Voltage_read) ENABLED START #
        return 0.0
        # PROTECTED REGION END #    //  PowerSupply.Voltage_read

    def write_Voltage(self, value):
        # PROTECTED REGION ID(PowerSupply.Voltage_write) ENABLED START #
        pass
        # PROTECTED REGION END #    //  PowerSupply.Voltage_write

    def read_Current(self):
        # PROTECTED REGION ID(PowerSupply.Current_read) ENABLED START #
        return 0.0
        # PROTECTED REGION END #    //  PowerSupply.Current_read

    def read_LoadImpedance(self):
        # PROTECTED REGION ID(PowerSupply.LoadImpedance_read) ENABLED START #
        return 0.0
        # PROTECTED REGION END #    //  PowerSupply.LoadImpedance_read


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(PowerSupply.main) ENABLED START #
    return run((PowerSupply,), args=args, **kwargs)
    # PROTECTED REGION END #    //  PowerSupply.main

if __name__ == '__main__':
    main()
