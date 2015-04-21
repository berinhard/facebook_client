#coding:utf-8
from unittest import TestCase

from facebook_client.client import FacebookGraphApiClient, EventsApi


class MockedSession(object):

    def get(self, *args, **kwargs):
        pass


class TestEventsApi(TestCase):

    def setUp(self):
        self.session = MockedSession()
        self.client = EventsApi(self.session)

    def test_object_is_created_correctly(self):
        self.assertEqual('/', self.client.base_path)
        self.assertEqual(self.session, self.client.session)


class TestFacebookGraphApi(TestCase):

    def setUp(self):
        self.client = FacebookGraphApiClient('xpto')

    def test_recovers_events_client_correctly(self):
        events_client = self.client.events
        self.assertIsInstance(events_client, EventsApi)
        self.assertEqual('xpto', events_client.session.access_token)
