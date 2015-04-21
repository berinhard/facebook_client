# coding:utf-8
from requests import Session


class FacebookSession(Session):

    def __init__(self, *args, **kwargs):
        try:
            self.access_token = kwargs.pop('access_token')
        except KeyError:
            raise TypeError(u'You need to pass the access_token parameter to use the API.')
        super(FacebookSession, self).__init__(*args, **kwargs)

    def _get_full_url(self, path):
        return "https://graph.facebook.com/v2.3{}".format(path)

    def request(self, method, url, params=None, *args, **kwargs):
        params = params or {}
        params['access_token'] = self.access_token
        full_url = self._get_full_url(url)
        r = super(FacebookSession, self).request(method, full_url, params, *args, **kwargs)
        return FacebookResponse(status_code=r.status_code, data=r.json())


class FacebookResponse(object):

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data
