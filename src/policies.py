from collections import deque, OrderedDict

def fifo(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for item in requests:
        if item in cache:
            # Cache hit
            continue
        else:
            # Cache miss
            misses += 1

            # Remove the oldest item if the cache is full
            if len(cache) >= k:
                oldest = order.popleft()
                cache.remove(oldest)
            
            # Add the new item to the cache and order
            cache.add(item)
            order.append(item)

    return misses

def lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for item in requests:
        if item in cache:
            # Cache hit
            cache.move_to_end(item)
        else:
            # Cache miss
            misses += 1

            if len(cache) >= k:
                # Remove the least recently used item
                cache.popitem(last=False)
            # Add the new item to the end as the most recently used
            cache[item] = True

    return misses

def optff(k, requests):
   misses = 0

   return misses 
