#!/usr/bin/env python2
from sys import stdin, stdout
from json import loads
import re


def read():
    parse_line = re.compile('(\d+)\t(.*)')

    line = stdin.readline()
    while line:
        m = parse_line.match(line)
        if m:
            node = int(m.group(1))
            data = loads(m.group(2))

            stdout.write("%d\t%f\n" % (node, data['p']))

        line = stdin.readline()


if __name__ == '__main__':
    read()
