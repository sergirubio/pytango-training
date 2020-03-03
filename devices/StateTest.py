# -*- coding: utf-8 -*-
#
# This file is part of the StateTest project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" StateTest

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
# PROTECTED REGION ID(StateTest.additionnal_import) ENABLED START #
import time
# PROTECTED REGION END #    //  StateTest.additionnal_import

__all__ = ["StateTest", "main"]


class StateTest(SKABaseDevice):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(StateTest.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  StateTest.class_variable

    # -----------------
    # Device Properties
    # -----------------





    # ----------
    # Attributes
    # ----------









    Now = attribute(
        dtype='double',
    )


    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        SKABaseDevice.init_device(self)
        # PROTECTED REGION ID(StateTest.init_device) ENABLED START #
        self.set_state(DevState.ON)
        self.set_change_event('State',True,False)
        self.set_change_event('Now',True,False)
        # PROTECTED REGION END #    //  StateTest.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(StateTest.always_executed_hook) ENABLED START #
        #self.push_change_event('Now',time.time())
        pass
        # PROTECTED REGION END #    //  StateTest.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(StateTest.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  StateTest.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Now(self):
        # PROTECTED REGION ID(StateTest.Now_read) ENABLED START #
        self.set_state(DevState.RUNNING)
        self.push_change_event('State')
        time.sleep(.1)
        t = time.time()
        self.set_state(DevState.ON)
        self.push_change_event('State')
        return t
        # PROTECTED REGION END #    //  StateTest.Now_read


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(StateTest.main) ENABLED START #
    return run((StateTest,), args=args, **kwargs)
    # PROTECTED REGION END #    //  StateTest.main

if __name__ == '__main__':
    main()
