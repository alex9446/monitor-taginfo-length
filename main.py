from hash import hash_values
from heartbeat import send_heartbeat
from taginfo import get_tag_values
from telegram import (broadcast_message, escape_markdown_v2, get_description,
                      get_short_description, set_description)

send_heartbeat(start_signal=True)

short_description = get_short_description()
description = get_description()

monitored_tags_raw = short_description.split(',')
saved_tags = {parts[0]: parts[1] for line in description.splitlines()
              if (parts := line.split('='))}

monitored_tags = [(tag, get_tag_values(tag)) for tag in monitored_tags_raw]
hashed_tags = [(key, hash_values(values)) for key, values in monitored_tags]

for key, hash in hashed_tags:
    escaped_key = escape_markdown_v2(key)
    if key not in saved_tags:
        broadcast_message(f'new tag: *{escaped_key}*')
    elif hash != saved_tags[key]:
        broadcast_message(f'edited tag: *{escaped_key}*')

hashed_tags_raw = '\n'.join(f'{key}={hash}' for key, hash in hashed_tags)
set_description(hashed_tags_raw)

send_heartbeat()
