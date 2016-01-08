#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from json import loads, dumps
import re


def mapper():
    mm = 0
    is_a_row = re.compile('(\d+)\t(.*)')
    line = stdin.readline()
    while line:
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            if src == 0:
                mm += float(m.group(2))
            else:
                d = loads(m.group(2))
                if d:
                    d['mm'] = mm
                    stdout.write("%s\t%s\n" % (src, dumps(d)))
        d = None
        line = stdin.readline()

if __name__ == '__main__':
    mapper()