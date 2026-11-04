from os import getenv

from requests import get


def send_heartbeat(start_signal: bool = False) -> bool:
    req_url = getenv('HEARTBEAT_URL')
    if not req_url:
        print('heartbeat url not found!')
        return False
    path = '/start' if start_signal else ''
    return get(req_url + path).ok
