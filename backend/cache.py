import time
_cache = {}
TTL = 300
MAX_CACHE = 1000
def get(key):
    entry = _cache.get(key)
    if not entry:
        return None
    value, timestamp = entry
    if time.time() - timestamp > TTL:
        del _cache[key]
        return None
    return value
def set(key, value):
    if len(_cache) > MAX_CACHE:
        _cache.clear()

    _cache[key] = (value, time.time())
def clear():
    _cache.clear()