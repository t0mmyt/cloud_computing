#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from json import loads, dumps
import re


def reducer():
    is_a_row = re.compile('(\d+)\t(.*)')
    line = stdin.readline()
    pr = dict()
    while line:
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            if src != 0:
                d = loads(m.group(2))
                if d:
                    pr[src] = d['pr']
        line = stdin.readline()

    i = 0
    for src in sorted(pr, key=pr.get, reverse=True):
        if i > 10:
            break
        stdout.write("%s\t%s\n" % (src, pr[src]))
        i += 1

if __name__ == '__main__':
    reducer()