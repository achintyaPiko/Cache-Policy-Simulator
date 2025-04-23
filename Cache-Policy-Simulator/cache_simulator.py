import random

class CacheSimulator:


    #   IMPORTANT NOTES TO KEEP IN MIND:
    #   NO BIT ADDRESS DECOMPOSITION IS IMPLEMENTED 
    #   IE THE ADDRESS IS NOT ONLY USED TO FIND THE SET BUT IS ALSO USED AS THE DATA THAT IS GOING TO BE STORED IN THE CACHE LINE AKA 
    #   |    TAG     |    INDEX    |    BO    | 
    #   FORMAT OF ADDRESSING IS NOT USED 
    
    def __init__(self, cache_size, associativity,rule):
        self.cache_size = cache_size
        self.associativity = associativity
        self.num_sets = cache_size // associativity

        # list of list, represent a cache with lines
        self.sets = [[] for _ in range(self.num_sets)]

        # Stats
        self.hits = 0
        self.misses = 0
        self.rule = rule

    def _get_set_index(self, address):
        return address % self.num_sets
    

    def lookup(self, address):
        
        set_index = self._get_set_index(address)
        cache_set = self.sets[set_index]

        if (address in cache_set and self.rule != 'LRU'):
            # cache hit
            return True, set_index
        elif (address in cache_set and self.rule == 'LRU'):
            # LRU is actually being implemented here with the most recent data that is a hit being moved to the top by remove and append to denote a MRU data
            cache_set.remove(address)
            cache_set.append(address)
            return True, set_index
        else:
            
            # cache miss                                    
            if len(cache_set) >= self.associativity:
                # cache is full and something needs to be evicted. What rules are going to be used are going to differ
                evicted =  self.evict(self.rule,set_index)
            else:
                # cache wasnt full just data wasnt there do nothing
                evicted = None
                
            # new data added
            cache_set.append(address)
            return False, set_index
            

    def access(self, address):
        hit, set_index = self.lookup(address)
        if hit:
            self.hits += 1
            """
            Uncomment below code If you want simultaneous Hit Text
            print(f"HIT: Address {address} found in set {set_index}")
            """
        else:
            self.misses += 1
            """
            Uncomment below code If you want simultaneous Miss Text
            print(f"MISS: Address {address} inserted into set {set_index}")
            """
    def randomReplacement(self, set_index):
        victim_set = self.sets[set_index]
        idx = random.randint(0, len(victim_set) - 1)
        evicted = victim_set.pop(idx)
        return evicted

    def fifoReplacement(self, set_index):
        victim_set = self.sets[set_index]
        evicted = victim_set.pop(0)
        return evicted

    def lruReplacement(self, set_index):
        victim_set = self.sets[set_index]
        evicted = victim_set.pop(0)
        #behavior of fifoReplacement and lruReplacement is same but actual LRU is implemented in the hit miss detection block
        return evicted

    def evict(self,policy,set_index):
        if(policy == "RR"):
            evict = self.randomReplacement(set_index)
        elif(policy == "FIFO"):
            evict = self.fifoReplacement(set_index)
        elif(policy=="LRU"):
            evict = self.lruReplacement(set_index)
        return evict
    
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

        