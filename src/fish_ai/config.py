# -*- coding: utf-8 -*-
from os import path
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read(path.expanduser('~/.config/fish-ai.ini'))


def lookup_setting():
    print(get_config(sys.argv[1] or ''))


def get_config(key):
    if not config.has_section('fish-ai'):
        # There is no configuration file or the user made a mistake.
        # Just return 'None' here to simplify testing.
        return None

    active_section = config.get(section='fish-ai', option='configuration')

    if config.has_option(section=active_section, option=key):
        return config.get(section=active_section, option=key)

    return config.get(section='fish-ai', option=key, fallback=None)