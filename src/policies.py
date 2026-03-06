from collections import deque, OrderedDict
import heapq

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


# Citation: https://www.geeksforgeeks.org/python/max-heap-in-python/, https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/
def future_request(requests, start, item):
    # heapq is minHeap, use negative to simulate maxHeap

    for i in range(start+1, len(requests)):
        if requests[i] == item: # Called again
            return -(i - start)
        
    return float('-inf') # Never appeared


def optff(k, requests):
    misses = 0
    cache = []
    
    # If the item is already in the cache, this is a hit.
    for index, item in enumerate(requests):
        # Cache hit
        if item in cache:
            continue
       
        # Cache Miss
        else:
            misses += 1
           
            # Cache not full, simply insert
            if len(cache) < k:
                cache.append(item)
            
            else:
                # Eviction Policy:
                # Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).

                # Citation: https://www.geeksforgeeks.org/python/max-heap-in-python/, https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/
                heap = []
                
                # Build Heap
                for cachedItem in cache:
                    # nextRequest is the Priority
                    nextRequest = future_request(requests, index, cachedItem)
                    heapq.heappush(heap, (nextRequest, cachedItem))

                maxRequest, maxHeap = heapq.heappop(heap) # maxRequest is negative still
                cache.remove(maxHeap)

                # Add the new item to the cache
                cache.append(item)

    return misses