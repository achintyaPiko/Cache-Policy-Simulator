class CacheSimulator:
    def __init__(self, cache_size, replacement_policy):
        self.cache_size = cache_size
        self.replacement_policy = replacement_policy
        self.cache = [None] * cache_size

    def access(self, address):
        """Handle memory access based on the replacement policy."""
        raise NotImplementedError("Access method not implemented.")

    def stats(self):
        """Print final cache statistics."""
        pass
