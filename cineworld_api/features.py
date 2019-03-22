#!/usr/bin/env python3
"""
features.py - All the endpoints
"""
import datetime


class Features(object):
    """
    """

    def search_cinemas_by_name(self, name):
        """Search for cinemas
        By name
        By id
        By date i.e. get all cinemas open on that date
        """
        cinemas = self.get_cinemas()
        for cinema in cinemas['cinemas']:
            if name.lower() in cinema['displayName'].lower():
                return cinema
        return None

    def search_movies_by_name(self, cinema_id, date, name):
        """Search for movies
        """
        movies = self.get_movies(cinema_id, date=date)
        for movie in movies['films']:
            if name.lower() in movie['name'].lower():
                return movie['id']
        return None
