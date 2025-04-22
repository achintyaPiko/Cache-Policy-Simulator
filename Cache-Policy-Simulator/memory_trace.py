def load_trace(file_path):
    """Load memory addresses from file."""
    with open(file_path, 'r') as f:
        trace = [int(line.strip()) for line in f.readlines()]
    return trace
