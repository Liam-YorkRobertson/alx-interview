#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict

def process_logs():
    """
    function that does log parsing
    """
    total_size = 0
    status_counts = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                _, _, _, _, _, status, size = line.split(maxsplit=6)
                if "GET /projects/260 HTTP/1.1" in line:
                    total_size += int(size)
                    status_counts[status] += 1

                if i % 10 == 0:
                    print(f"File size: {total_size}")
                    print('\n'.join(f"{code}: {count}" for code, count in sorted(status_counts.items())))

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        pass

    print(f"File size: {total_size}")
    print('\n'.join(f"{code}: {count}" for code, count in sorted(status_counts.items())))

if __name__ == "__main__":
    process_logs()
