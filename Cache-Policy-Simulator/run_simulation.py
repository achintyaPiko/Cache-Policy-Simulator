import argparse
from memory_trace import load_trace
from cache_simulator import CacheSimulator

def main():
    parser = argparse.ArgumentParser(description="Cache Replacement Policy Simulator")
    parser.add_argument('--policy', type=str, required=True, help='Replacement policy: FIFO ( keyword: FIFO ) | LRU | Random ( keyword: RR )')
    parser.add_argument('--cache-size', type=int, required=True, help='Cache size in number of blocks')
    parser.add_argument('--associativity', type=int, required=True, help='Associativity number')
    parser.add_argument('--trace', type=str, required=True, help='Path to memory access trace file')
    
    args = parser.parse_args()

    print(f"Running simulation with {args.policy} policy and cache size {args.cache_size}")
    
    traceFile = load_trace(args.trace)
    cache = CacheSimulator(args.cache_size,args.associativity,args.policy)

    for data in traceFile:
        cache.access(data)
    print(cache.get_stats())


if __name__ == "__main__":
    main()
