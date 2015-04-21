#coding:utf-8
from mock import patch, Mock
from requests import Session
from unittest import TestCase

from facebook_client.request import FacebookSession, FacebookResponse


class MockedRequestsResponse(object):
    status_code = 200

    def json(self):
        return {'key': 'value'}


class TestFacebookSession(TestCase):

    def setUp(self):
        self.access_token = 'access_token'
        self.session = FacebookSession(access_token=self.access_token)

    def test_raises_type_error_if_access_token_is_not_provided(self):
        self.assertRaises(TypeError, FacebookSession)

    def test_builds_full_url_correctly(self):
        path = '/path/'
        expected_ul = 'https://graph.facebook.com/v2.3/path/'

        url = self.session._get_full_url(path)
        self.assertEqual(expected_ul, url)

    @patch.object(Session, 'request')
    def test_adds_access_token_to_params_if_no_params_provided(self, mocked_super_request):
        mocked_super_request.return_value = MockedRequestsResponse()
        self.session.request('GET', '/path/')

        url = self.session._get_full_url('/path/')
        mocked_super_request.assert_called_once_with('GET', url, {'access_token': self.access_token})

    @patch.object(Session, 'request')
    def test_adds_access_token_to_params_if_without_losing_params(self, mocked_super_request):
        mocked_super_request.return_value = MockedRequestsResponse()
        self.session.request('GET', '/path/', params={'key': 'value'})

        url = self.session._get_full_url('/path/')
        expected_params = {'access_token': self.access_token, 'key': 'value'}
        mocked_super_request.assert_called_once_with('GET', url, expected_params)

    @patch.object(Session, 'request', Mock(return_value=MockedRequestsResponse()))
    def test_returns_custom_response_object(self):
        response = self.session.request('GET', '/path/', params={'key': 'value'})

        self.assertIsInstance(response, FacebookResponse)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'key': 'value'}, response.data)
