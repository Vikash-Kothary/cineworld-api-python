#!/usr/bin/env python3
"""
tests/test_config.py - Test config values
"""

import os
from cineworld_api.config import Config


def test_host_up():
    """Test server url is a valid, up and running
    """
    r = os.system('ping -c 1 ' + Config.BASE_URL)
    assert r != 0, 'Server is down or incorrect'


def test_user_agent():
    expected = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    # actual = Config.USER_AGENT
    #assert expected == actual
