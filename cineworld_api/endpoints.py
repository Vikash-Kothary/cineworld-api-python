#!/usr/bin/env python3
"""
endpoints.py - All the endpoints
"""
import requests
import datetime


class Endpoints(object):
    """
    """

    def get_cinemas(self, date=None):
        """Returns all cinemas with events within the next year
        """
        if date == None:
            today = datetime.datetime.now()
            date = today.replace(year=today.year + 1).strftime("%Y-%m-%d")
        endpoints = '/cinemas/with-event/until/{date}'.format(date=date)
        return self.get_request(endpoints)

    def get_dates(self, cinema, date=None):
        """Returns all dates with events within the next year
        """
        if date == None:
            today = datetime.datetime.now()
            date = today.replace(year=today.year + 1).strftime("%Y-%m-%d")
        endpoints = '/dates/in-cinema/{cinema}/until/{date}'.format(cinema=cinema, date=date)
        return self.get_request(endpoints)

    def get_movies(self, cinema, date=None):
        """Returns information about all the movies showing and their show times
        """
        if date == None:
            today = datetime.datetime.now()
            date = today.strftime("%Y-%m-%d")
        endpoints = '/film-events/in-cinema/{cinema}/at-date/{date}'.format(
            cinema=cinema, date=date)
        return self.get_request(endpoints)

    def get_trailers(self, cinema):
        """Returns links for movies currently showing at cinema
        """
        endpoints = '/trailers/byCinemaId/{cinema}?{variable}'.format(
            cinema=cinema, variable='_=1543256932933')
        return self.get_request(endpoints)
