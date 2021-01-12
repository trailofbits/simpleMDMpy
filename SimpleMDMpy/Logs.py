#!/usr/bin/env python

"""Logs module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class Logs(SimpleMDMpy.SimpleMDM.Connection):
    """GET all the LOGS"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/logs")

    def get_logs(self, id_override=0):
        """And I mean all the LOGS"""
        url = self.url
        data = {}
        return self._get_data(url, data, id_override=id_override)