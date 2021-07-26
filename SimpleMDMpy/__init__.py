""" SimpleMDMpy - A python API for interacting with SimpleMDM API.
Your Simple MDM API is required."""
#pylint: disable=invalid-name
from .Account import Account
from .AppGroups import AppGroups
from .Apps import Apps
from .AssignmentGroups import AssignmentGroups
from .Cli import main
from .CustomAttributes import CustomAttributes
from .CustomConfigurationProfiles import CustomConfigurationProfiles
from .DepServers import DepServers
from .DeviceGroups import DeviceGroups
from .Devices import Devices
from .Enrollments import Enrollments
from .InstalledApps import InstalledApps
from .Logs import Logs
from .LostMode import LostMode
from .ManagedAppConfigs import ManagedAppConfigs
from .PushCertificate import PushCertificate

VERSION = "3.0.6"
