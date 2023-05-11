#!/usr/bin/python3
"""
log parser
"""
import sys


if __name__ == "__main__":
    file_size = [0]
    status_codes_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                           403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """Print the current stats"""
        print("File size: {}".format(file_size[0]))
        for key in sorted(status_codes_counts.keys()):
            if status_codes_counts[key]:
                print("{}: {}".format(key, status_codes_counts[key]))

    def parse_line(line):
        """checks the line for matches and parses it"""
        try:
            # remove the next line character at the end line
            line = line[:-1]
            # split line to words
            words = line.split(" ")
            # size of the line is the word, add it to file_size
            file_size[0] += int(words[-1])
            # status code comes second to the last
            status_code = int(words[-2])
            # increase status code coutn if it is in status_code_count
            if status_code in status_codes_counts:
                status_codes_counts[status_code] += 1
        except BaseException:
            pass

    line_number = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            # after every 10 lines, print report
            if line_number % 10 == 0:
                print_stats()
            line_number += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()