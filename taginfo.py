from requests import get

base = 'https://taginfo.openstreetmap.org/api/4/key/values?key='


def get_tag_values(key: str) -> list[str]:
    resp = get(f'{base}{key}').json()
    return [tag['value'] for tag in resp['data']]
