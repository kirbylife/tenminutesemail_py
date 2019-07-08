from datetime import datetime, timedelta

from requests import get

_HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers'
}


class TenMinutesEmail:
    _endpoint = "https://10minutemail.com/10MinuteMail/resources/session/{}".format

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        r = get("https://10minutemail.com/10MinuteMail/index.html",
                headers=_HEADERS)
        self.cookies = r.cookies

        r = get(self._endpoint("address"),
                cookies=self.cookies,
                headers=_HEADERS)
        self.address = r.text

    def __str__(self):
        return self.address

    def __repr__(self):
        return "({}, seconds_left={})".format(self.address,
                                              self.seconds_left())

    def is_alive(self, check_server=False):
        if check_server:
            r = get(self._endpoint("expired"),
                    cookies=self.cookies,
                    headers=_HEADERS)
            return r == "true"
        else:
            return (datetime.now() - self.updated_at) < timedelta(minutes=10)

    def reset_time(self):
        assert (self.is_alive())
        self.updated_at = datetime.now()
        get(self._endpoint("reset"), cookies=self.cookies, headers=_HEADERS)

    def seconds_left(self, check_server=False):
        assert (self.is_alive())
        if check_server:
            r = get(self._endpoint("secondsLeft"),
                    cookies=self.cookies,
                    headers=_HEADERS)
            return int(r.text)
        else:
            return int(600 -
                       (datetime.now() - self.updated_at).total_seconds())
