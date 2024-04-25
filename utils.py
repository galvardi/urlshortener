import hashlib

from constants import HASH_SIZE


def calculate_hash(st: str) -> str:
    h = hashlib.blake2s(digest_size=HASH_SIZE)
    h.update(st.encode())
    return h.hexdigest()
