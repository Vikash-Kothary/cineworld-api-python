#!/usr/bin/env python3
"""
config.py -
"""

import os


class Config:
    """Default Configuration
    """

    # DO NOT CHANGE UNLESS YOU KNOW WHAT YOU'RE DOING
    # Response Headers
    CONTENT_TYPE = 'application/json;charset=utf-8'
    X_APPLICATION_CONTEXT = 'data-api-service'  # :8430

    # Request Headers
    SCHEME = 'https'
    HOST = 'www.cineworld.co.uk'
    ACCEPT = 'application/json;charset=utf-8'
    # ACCEPT_ENCODING = 'jzip, deflate, br'
    # ACCEPT_LANGUAGE = 'en-GB, en;q=0.9'
    COUNTRY = 'uk'
    API_VERSION = 'v1'

    BASE_URL_FORMAT = '{scheme}://{host}/{country}/{application_context}/{api_version}/quickbook/10108'
    BASE_URL = BASE_URL_FORMAT.format(**{
        'scheme': SCHEME,
        'host': HOST,
        'country': COUNTRY,
        'application_context': X_APPLICATION_CONTEXT,
        'api_version': API_VERSION
    })

    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    # USER_AGENT_FORMAT = \
    #    '{app_name}/{app_version} ({device}; {os_name} {os_version}; {version_code})'
    # USER_AGENT = USER_AGENT_FORMAT.format(**{})

    # Query String Parameters
    LANG = 'en-GB'
