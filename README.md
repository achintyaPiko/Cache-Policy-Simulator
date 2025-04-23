# Cache Policy Simulator

This project implements a simulator for evaluating cache performance under different replacement strategies. It models a set-associative  cache and supports three widely used policies: FIFO (First-In-First-Out), LRU (Least Recently Used), and Random. The simulator helps analyze cache hit/miss rates using synthetic or user-defined memory access patterns.

## Features

- Set-associative cache simulation
- FIFO, LRU, and Random replacement strategies
- Support for custom memory access patterns
- Reports:
  - Total memory accesses
  - Cache hits and misses
  - Hit rate and miss rate
- Modular design for easy extensibility

## How It Works

Each simulation run accepts the following parameters:
- Cache size (number of blocks)
- Memory access trace (list of memory addresses)
- Cache replacement policy

The simulator processes the memory trace and reports cache performance statistics.

## Getting Started

### Requirements

- Python 3.6 or higher

(Optional)
- matplotlib (for visualizing results, if implemented later)

### Example Usage

```bash
python run_simulation.py --policy LRU --cache-size 8 --trace traces/sample_trace.txt
```
## References Used:
[Set-Associative Mapping](https://www.youtube.com/watch?v=mCF5XNn_xfA)
[NPTEL lectures](https://youtu.be/OwYyLhZWcgs)
