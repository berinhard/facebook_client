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

    def get_by_id(self, event_id):
        path = "{0}{1}/".format(self.base_path, event_id)
        response = self.session.get(path)
        return response
