class CacheSimulator:


    # line size not needed because no relation b/w block offset and hit miss ratio
    def __init__(self, cache_size, associativity):
        self.cache_size = cache_size
        self.associativity = associativity
        self.num_sets = cache_size // associativity

        # list of list, represent a cache with lines
        self.sets = [[] for _ in range(self.num_sets)]

        # Stats
        self.hits = 0
        self.misses = 0

    def _get_set_index(self, address):
        return address % self.num_sets

    def lookup(self, address):
        """Lookup an address in the cache and update cache state."""
        set_index = self._get_set_index(address)
        cache_set = self.sets[set_index]

        if address in cache_set:
            # Cache hit
            return True, set_index
        else:
            # Cache miss: apply placeholder replacement logic
            if len(cache_set) >= self.associativity:
                # Evict the first inserted block (FIFO for now)
                evicted = cache_set.pop(0)
            else:
                evicted = None
            cache_set.append(address)
            return False, set_index

    def access(self, address):
        hit, set_index = self.lookup(address)
        if hit:
            self.hits += 1
            print(f"HIT: Address {address} found in set {set_index}")
        else:
            self.misses += 1
            print(f"MISS: Address {address} inserted into set {set_index}")

    def get_stats(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total) * 100 if total else 0
        miss_rate = 100 - hit_rate
        return {
            "Total Accesses": total,
            "Cache Hits": self.hits,
            "Cache Misses": self.misses,
            "Hit Rate (%)": round(hit_rate, 2),
            "Miss Rate (%)": round(miss_rate, 2)
        }
