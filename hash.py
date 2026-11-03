from hashlib import blake2s


def short_hash(value: str) -> str:
    return blake2s(value.encode('utf-8'), digest_size=4).hexdigest()


def hash_values(values: list[str]) -> str:
    return short_hash('|'.join(sorted(values)))
