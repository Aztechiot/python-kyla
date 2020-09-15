"""Python interface for TP-Link's smart home devices.

All common, shared functionalities are available through `SmartDevice` class::

    x = SmartDevice("192.168.1.1")
    print(x.sys_info)

For device type specific actions `SmartBulb`, `SmartPlug`, or `SmartStrip`
 should be used instead.

Module-specific errors are raised as `SmartDeviceException` and are expected
to be handled by the user of the library.
"""
from importlib_metadata import version  # type: ignore
from kyla.discover import Discover
from kyla.exceptions import SmartDeviceException
from kyla.protocol import TPLinkSmartHomeProtocol
from kyla.smartbulb import SmartBulb
from kyla.smartdevice import DeviceType, EmeterStatus, SmartDevice
from kyla.smartdimmer import SmartDimmer
from kyla.smartlightstrip import SmartLightStrip
from kyla.smartplug import SmartPlug
from kyla.smartstrip import SmartStrip

__version__ = version("python-kyla")


__all__ = [
    "Discover",
    "TPLinkSmartHomeProtocol",
    "SmartBulb",
    "DeviceType",
    "EmeterStatus",
    "SmartDevice",
    "SmartDeviceException",
    "SmartPlug",
    "SmartStrip",
    "SmartDimmer",
    "SmartLightStrip",
]
