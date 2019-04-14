import os
import requests
import datetime
import warnings
import pandas as pd
from .exceptions import ApiKeyError, ResponseError


class PhishNetAPI:
    """
    Too lazy rn
    """

    def __init__(self):
        """
        Too lazy rn
        """
        self._api_key = os.environ.get('PHISH_API_KEY')
        self._base_url = 'https://api.phish.net/v3'
        self._request_limit = 120
        if self._api_key is None:
            raise ApiKeyError('No API key found. Check your environment'
                              'variables and try again.')
        else:
            self.has_api_key = True

    # ------------- Response Error Handling Utilities -------------

    def _is_ok_response(self, response):
        """
        Too lazy rn
        """
        if response.status_code == requests.codes.ok:
            pass
        else:
            response.raise_for_status()

    def _response_has_error(self, response):
        """
        Too lazy rn
        """
        json_response = response.json()
        if json_response.get('error_code') != 0:
            raise ResponseError(f"error code {json_response.get('error_code')}"
                                f": {json_response.get('error_message')}")

    # ------------- Query Parameter Utilities -------------

    def _add_api_key_to_query_params(self):
        """
        Too lazy rn
        doc: http://docs.python-requests.org/en/master/user/quickstart/
        """
        payload = {}
        payload['apikey'] = self._api_key
        return payload

    def _mask_api_key_from_url(self, response, payload):
        """
        Too lazy rn
        """

        url = response.url.replace(payload['apikey'], '<<apikey>>')

        return url

    def _mask_api_key_from_query_string(self, response, payload, endpoint):
        """
        Too lazy rn
        """

        masked_url = response.url.replace(payload['apikey'], '<<apikey>>')
        query_string = masked_url.replace(endpoint, '')
        return query_string

    # ------------- URL Utilities -------------

    def _append_endpoint(self, url, endpoint):
        """
        Too lazy rn
        """

        return url + endpoint

    # ------------- Endpoint methods (GET, POST) -------------

    def get_all_venues(self):
        """
        Too lazy rn
        """

        endpoint = '/venues/all'
        self.endpoint_ = self._append_endpoint(self._base_url, endpoint)

        payload = self._add_api_key_to_query_params()
        response = requests.request("GET", self.endpoint_, params=payload)

        self.url_ = self._mask_api_key_from_url(response, payload)
        self.query_string_ = self._mask_api_key_from_query_string(
            response, payload, self.endpoint_)

        self._is_ok_response(response)
        self._response_has_error(response)

        venues = pd.DataFrame(response.json().get(
            'response').get('data')).transpose()

        return venues

    def get_all_shows(self):
        """
        Utilize the Phish.net /shows/query/ endpoint to iteratively pull all shows by year and return as a dataframe
        """

        # define api endpoint
        endpoint = '/shows/query/'
        self.endpoint_ = self._append_endpoint(self._base_url, endpoint)

        # initialize dataframe to hold all shows
        all_shows = pd.DataFrame()

        # query all shows by year
        for year in range(1983, datetime.datetime.now().year+1):

            # construct payload
            payload = self._add_api_key_to_query_params()
            payload['year'] = year
            payload['order'] = 'ASC'

            # request data
            response = requests.request("GET", self.endpoint_, params=payload)

            # save attributes
            self.url_ = self._mask_api_key_from_url(response, payload)
            self.query_string_ = self._mask_api_key_from_query_string(
                response, payload, self.endpoint_)

            # check response
            self._is_ok_response(response)
            self._response_has_error(response)

            # if that year has 300 shows, warn us because we may be missing data because of API cutoff
            if response.json().get('response').get('count') >= 300:
                warnings.warn(f'The year {year} has 300 or more shows, this API query is missing data.')

            # format data
            this_year_shows = pd.DataFrame(response.json().get(
                'response').get('data'))

            # append this years shows to master dataframe
            all_shows = pd.concat([all_shows, this_year_shows], ignore_index=True)

        return all_shows


    def get_setlist(self, showid):
        """
        Given a showid, utilize the Phish.net /setlists/get/ endpoint to pull all show information and format into dataframe
        """

        # define api endpoint
        endpoint = '/setlists/get'
        self.endpoint_ = self._append_endpoint(self._base_url, endpoint)

        # construct payload
        payload = self._add_api_key_to_query_params()
        payload['showid'] = showid

        # request data
        response = requests.request("GET", self.endpoint_, params=payload)

        # save attributes
        self.url_ = self._mask_api_key_from_url(response, payload)
        self.query_string_ = self._mask_api_key_from_query_string(
            response, payload, self.endpoint_)

        # check response
        self._is_ok_response(response)
        self._response_has_error(response)

        # format data
        setlist = pd.DataFrame(response.json().get(
            'response').get('data'))

        return setlist
