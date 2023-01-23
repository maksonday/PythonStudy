import sys
import re
import argparse


class Params:
    def __init__(self, pattern):
        self.pattern = pattern


def output(line):
    print(line)


def _ignore_(line, pattern):
    if re.I.search(pattern, line):
        return True
    else:
        return False


def _invert_(line, pattern):
    if re.search(pattern, line):
        return False
    else:
        return True


def _count_(lines, pattern):
    count = 0
    for line in lines:
        if re.search(pattern, line):
            count += 1
    return count


def grep(lines, params):
    for line in lines:
        line = line.rstrip()
        if params['pattern'] in line:
            output(line)


def parse_args(args):
    params = dict
    args = args.split()
    params['pattern'] = args.pop(0)
    for p in args:
        params[p] = True
    return params


def main():
    parser = argparse.ArgumentParser(
        prog='grep',
        description='regex search util',
    )
    parser.add_argument('-i', action=argparse.BooleanOptionalAction)
    parser.add_argument('-v', action=argparse.BooleanOptionalAction)
    parser.add_argument('-c', action=argparse.BooleanOptionalAction)
    parser.add_argument('-n', action=argparse.BooleanOptionalAction)
    parser.add_argument('-A', action='store', type=int)
    parser.add_argument('-B', action='store', type=int)
    parser.add_argument('-C', action='store', type=int)
    params = parser.parse_args()
    print(params)
    while 1:
        grep(sys.stdin.readline(), params)


main()

