#!/usr/bin/env python3
"""
tests/test_endpoints.py - Test endpoints
"""

import pytest
import vcr
from cineworld_api.client import Client
from cineworld_api.utils import FileUtils

VCR_BASE_PATH = './tests/vcr_cassettes'


@pytest.fixture
def cineworld_client():
    """Returns testing client
    """
    return Client()


@vcr.use_cassette(VCR_BASE_PATH + '/get_cinemas.yml')
def test_get_cinemas(cineworld_client):
    """Test get_cinemas()
    """
    response = cineworld_client.get_cinemas()
    FileUtils.save_json_to_file(response, VCR_BASE_PATH + '/get_cinemas.json')

    assert isinstance(response, dict)
