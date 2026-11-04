import re
from os import environ

from requests import get, post

bot_token = environ['BOT_TOKEN']
chat_ids = environ['CHAT_IDS'].split(',')

base = f'https://api.telegram.org/bot{bot_token}'


def _bot_get(endpoint: str, key: str) -> str:
    resp = get(f'{base}{endpoint}').json()
    if not resp['ok']:
        raise RuntimeError('response is not ok')
    return resp['result'][key]


def get_short_description():
    return _bot_get('/getMyShortDescription', 'short_description')


def get_description():
    return _bot_get('/getMyDescription', 'description')


def _bot_post(endpoint: str, key: str, value: str) -> bool:
    return post(f'{base}{endpoint}', json={key: value}).ok


def set_description(value: str):
    _bot_post('/setMyDescription', 'description', value)


def broadcast_message(text: str) -> None:
    for chat in chat_ids:
        post(f'{base}/sendMessage', json={
            'chat_id': chat,
            'text': text,
            'parse_mode': 'MarkdownV2'
        })


def escape_markdown_v2(text: str) -> str:
    escape_chars = r'_*[]()~`>#+-=|{}.!\\'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)
