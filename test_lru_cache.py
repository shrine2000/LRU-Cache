from lru_cache import LRUCache


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    assert cache.get(1) == 1

    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(3, 3)  # this should evict key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3

    cache.put(2, 20)
    assert cache.get(2) == 20

    # capacity 1
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)  # evict key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # non-existent key
    cache = LRUCache(2)
    assert cache.get(99) == -1


if __name__ == "__main__":
    test_lru_cache()
