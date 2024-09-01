#!/usr/bin/python3
"""
Log Parsing Script

This script reads lines from standard input and computes metrics based
on a specific log format.

The expected log format is: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>

Lines that do not match this format are skipped.

After every 10 lines or upon a keyboard interruption (CTRL + C),
the script prints the following statistics:
- Total file size: The sum of all <file size> values from the logs
- Number of lines by status code: Counts of lines for specific status codes
(200, 301, 400, 401, 403, 404, 405, and 500)

Status codes that do not appear or are not integers are not printed.
"""
import sys
import re
from collections import defaultdict


# Define the regular expression pattern for the log format
log_pattern = re.compile(
    r'(\d{1,3}\.){3}\d{1,3} - \['
    r'(.*?)\] "GET \/projects\/260 HTTP\/1\.1" '
    r'(\d{3}) (\d+)'
)

# Initialize variables for storing metrics
total_file_size = 0
status_counts = defaultdict(int)
lines_processed = 0


def print_statistics():
    """
    Prints the total file size and the number of lines by
    status code in ascending order.
    """
    global total_file_size, status_counts
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update metrics
            total_file_size += file_size
            status_counts[status_code] += 1

            lines_processed += 1

            # Print statistics every 10 lines
            if lines_processed % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Print statistics on keyboard interrupt
    print_statistics()
    sys.exit(0)

# Print statistics after the last line if it's not already printed
if lines_processed % 10 != 0:
    print_statistics()
