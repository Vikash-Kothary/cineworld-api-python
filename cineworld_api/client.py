#!/usr/bin/env python3
"""
client.py - API Client
"""

import requests
import json

from cineworld_api.config import Config
from cineworld_api.utils import FBUtils
from cineworld_api.errors import RequestError
from cineworld_api.endpoints import Endpoints
from cineworld_api.features import Features


class Client(Endpoints, Features, object):
    """API Client"""

    def __init__(self, username=None, password=None):
        """
        """
        self.headers = {
            "content-type": Config.CONTENT_TYPE,
            "User-agent": Config.USER_AGENT,
            "Accept": "text/html",

        }
        '?attr=&lang={lang}'.format(lang=Config.LANG)

    def get_request(self, path):
        """"""
        r = requests.get(Config.BASE_URL + path)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()['body']

    def post_request(self, path, params=None):
        """"""
        r = {}
        if params == None:
            r = requests.post(Config.BASE_URL + path)
        else:
            data = json.dumps(params)
            r = requests.post(Config.BASE_URL + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def put_request(self, path, params):
        """"""
        data = json.dumps(params)
        r = requests.put(Config.BASE_URL + path, headers=self.headers, data=data)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()

    def delete_request(self, path):
        """"""
        r = requests.delete(Config.BASE_URL + path, headers=self.headers)
        if (r.status_code != 200):
            raise RequestError(path)
        return r.json()
