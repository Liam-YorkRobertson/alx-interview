#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import re


def display_statistics(log):
    """
    displays the stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


def parse_logs():
    """
    parses logs
    """
    ip_address_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    date_time_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\]'
    request_line_pattern = r'"GET /projects/260 HTTP/1.1"'
    status_code_and_size_pattern = r'(.{3}) (\d+)'
    regex_pattern = (
        f'{ip_address_pattern} - '
        f'{date_time_pattern} '
        f'{request_line_pattern} '
        f'{status_code_and_size_pattern}'
    )
    log_regex = re.compile(regex_pattern)

    line_count = 0
    log = {"file_size": 0, "code_frequency":
           {str(code): 0 for code in
            [200, 301, 400, 401, 403, 404, 405, 500]}}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_regex.fullmatch(line)
            if match:
                line_count += 1
                code, file_size = match.group(1), int(match.group(2))
                log["file_size"] += file_size
                log["code_frequency"][code] += code.isdecimal()
                if line_count % 10 == 0:
                    display_statistics(log)
    finally:
        try:
            display_statistics(log)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    parse_logs()