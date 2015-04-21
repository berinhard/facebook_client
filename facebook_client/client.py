# coding:utf-8
from request import FacebookSession


class FacebookGraphApiClient(object):

    def __init__(self, access_token):
        session = FacebookSession(access_token=access_token)
        self.events = EventsApi(session)


class EventsApi(object):
    base_path = '/'

    def __init__(self, session):
        self.session = session
