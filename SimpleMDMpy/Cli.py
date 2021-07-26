from abc import ABC, abstractmethod
import argparse
from getpass import getpass
import sys
from typing import Dict, Optional

import keyring

from .Devices import Devices


KEYRING_NAME: str = "SimpleMDMpy"


class CliCommand(ABC):
    name: str
    help: str
    _api_key: Optional[str] = None

    def __init_subclass__(cls, **kwargs):
        if not cls.name or not cls.help:
            raise TypeError("Subclasses of CliCommand must define a `name` and a `help`")
        elif cls.name in COMMANDS:
            raise TypeError(f"CLI command \"{cls.name}\" is already defined in class "
                            f"{COMMANDS[cls.name].__class__.__name__}")
        COMMANDS[cls.name] = cls()

    @classmethod
    def prompt_for_api_key(cls) -> str:
        cls._api_key = keyring.get_password(KEYRING_NAME, "SimpleMDMKey")
        if cls._api_key is None:
            if not sys.stderr.isatty() or not sys.stdin.isatty():
                raise ValueError("Could not prompt for an API key because STDERR and STDIN are not a TTY")
            cls._api_key = getpass("SimpleMDM API Key: ", stream=sys.stderr)
            while True:
                sys.stderr.write("Would you like to save this password to the system keychain? [Yn] ")
                choice = input().lower().strip()
                if choice == "n":
                    sys.stderr.write("New API key will only be used for this session.\n")
                    break
                elif choice == "" or choice == "Y":
                    keyring.set_password(KEYRING_NAME, "SimpleMDMKey", cls._api_key)
                    sys.stderr.write("New API key saved to the system keychain.\n")
                    break
        return cls._api_key

    @classmethod
    def api_key(cls) -> str:
        if cls._api_key is not None:
            return cls._api_key
        return cls.prompt_for_api_key()

    @abstractmethod
    def run(self):
        raise NotImplementedError()


COMMANDS: Dict[str, CliCommand] = {}


def main():
    parser = argparse.ArgumentParser()

    keys = parser.add_mutually_exclusive_group(required=False)
    keys.add_argument("--key", "-k", type=str, help="use the provided API key; if omitted, a previously saved key "
                                                    "from the system keyring will be loaded; if no key has ever been "
                                                    "saved and STDIN is a TTY, the user will be prompted for a key")
    keys.add_argument("--prompt-for-key", "-p", action="store_true", help="prompt for an API key even if one is "
                                                                          "already saved in the system keychain")
    parser.add_argument("--version", "-v", action="store_true", help="print the version and exit")

    commands = parser.add_subparsers(help="SimpleMDM subcommands")
    for command in COMMANDS.values():
        p = commands.add_parser(command.name, help=command.help)
        p.set_defaults(func=command.run)

    args = parser.parse_args()

    if hasattr(args, "key") and args.key:
        CliCommand._api_key = args.key

    if args.version:
        from . import VERSION
        print(f"simplemdm {VERSION}")
        exit(0)
    elif args.prompt_for_key:
        CliCommand.prompt_for_api_key()

    if hasattr(args, "func"):
        args.func()


class ListDevices(CliCommand):
    name = "list"
    help = "list managed devices"

    def run(self):
        devices = Devices(self.api_key())

        for device in devices.get_device():
            attributes = device['attributes']

            # ugly API query to get username
            c = devices.get_custom_attribute(device['id'], '')  # returns a list of dicts
            email = ""
            for attribute in c:
                if attribute['id'] == 'username':
                    email = attribute['attributes']['value']

            print(device['id'],
                  "\"%s\"" % email,
                  "\"%s\"" % attributes['device_name'],
                  "\"%s\"" % attributes['model'],
                  "\"%s\"" % attributes['model_name'],
                  "\"%s\"" % attributes['serial_number'],
                  "\"%s\"" % attributes['os_version'],
                  "\"%s\"" % attributes['available_device_capacity'],
                  "\"%s\"" % attributes['is_cloud_backup_enabled'],
                  sep=",")


if __name__ == "__main__":
    main()
