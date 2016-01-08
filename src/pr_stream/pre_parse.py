#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from json import dumps
import re


def reducer():
    """
    Pre-parser to emit "NodeID  {pr, n, outlinks}" per edge

    Null Mapper and single reducer (needs to count n)
    """
    adj_out = dict()
    adj_in = dict()
    is_a_row = re.compile('(\d+)\t(\d+)')

    line = stdin.readline()
    while line:
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            dst = int(m.group(2))

            # Append to out list
            if src not in adj_out:
                adj_out[src] = []
            adj_out[src].append(dst)

            # Append to in list
            if dst not in adj_in:
                adj_in[dst] = []
            adj_in[dst].append(src)

        line = stdin.readline()

    # How many nodes?
    n = len(set(adj_in.keys() + adj_out.keys()))

    # Initial PR
    pr = 1.0/n

    # Emit
    for src, dsts in adj_out.items():
        stdout.write("%s\t%s\n" % (src, dumps(dict(
            pr=pr,
            n=n,
            out=dsts))))

if __name__ == '__main__':
    reducer()
