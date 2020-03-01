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
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(FixedCurrentPowerSupply.additionnal_import) ENABLED START #
import threading, time
# PROTECTED REGION END #    //  FixedCurrentPowerSupply.additionnal_import

__all__ = ["FixedCurrentPowerSupply", "main"]


class FixedCurrentPowerSupply(Device):
    """
    A dummy power supply for testing
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(FixedCurrentPowerSupply.class_variable) ENABLED START #
    
    def ramp_current(self,start, end):
        step = float(end-start)/self.RampingSteps                                                        
        self.set_state(DevState.RUNNING)
        for i in range(self.RampingSteps):
            time.sleep(1.)
            self.current += step
            self.push_change_event('Current',self.current)
            print(self.current)
        self.set_state(DevState.ON)
    
    # PROTECTED REGION END #    //  FixedCurrentPowerSupply.class_variable

    # -----------------
    # Device Properties
    # -----------------

    LoadImpedance = device_property(
        dtype='double', default_value=100
    )

    RampingSteps = device_property(
        dtype='double', default_value=10
    )

    StepTime_ms = device_property(
        dtype='int', default_value=1000
    )

    # ----------
    # Attributes
    # ----------

    Current = attribute(
        dtype='double',
        access=AttrWriteType.READ_WRITE,
    )

    Voltage = attribute(
        dtype='double',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        self.set_change_event("Current", True, False)
        # PROTECTED REGION ID(FixedCurrentPowerSupply.init_device) ENABLED START #
        self.set_state(DevState.OFF)
        self.current = 0.0
        self.voltage = 0.0
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Current(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.Current_read) ENABLED START #
        return self.current
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.Current_read

    def write_Current(self, value):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.Current_write) ENABLED START #
        if self.get_state() == DevState.OFF:
            raise Exception("PS is OFF!")
        
        if self.RampingSteps > 0:
            self.ramp_thread = threading.Thread(
                target = self.ramp_current,
                args = (self.current, value),
                )
            self.ramp_thread.start()
        else:
            self.current = 0
            self.push_change_event('Current',self.current)
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.Current_write

    def read_Voltage(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.Voltage_read) ENABLED START #
        if self.get_state() == DevState.OFF:
            return 0
        return self.current * self.LoadImpedance
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.Voltage_read


    # --------
    # Commands
    # --------

    @command(
    )
    @DebugIt()
    def On(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.On) ENABLED START #
        self.set_state(DevState.ON)
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.On

    @command(
    )
    @DebugIt()
    def Off(self):
        # PROTECTED REGION ID(FixedCurrentPowerSupply.Off) ENABLED START #
        self.set_state(DevState.OFF)
        # PROTECTED REGION END #    //  FixedCurrentPowerSupply.Off

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(FixedCurrentPowerSupply.main) ENABLED START #
    return run((FixedCurrentPowerSupply,), args=args, **kwargs)
    # PROTECTED REGION END #    //  FixedCurrentPowerSupply.main

if __name__ == '__main__':
    main()
