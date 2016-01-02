#!/usr/bin/env python2
from sys import stdin, stdout
import re
import json


def pre_parse():
    """
    Reads original file on stdin, calculates initial PR as 1/n and outputs adjeceny list with each inbound PR stored
    for every node in the format:

    dest    [[N1, PR1], [N2, PR2], ... [Nn, PRn]]
    (Value is JSON serialised)

    Although not space/bandwidth efficient, it allows each node to be processed independently.  Using Pickle(2) would be
    much more efficient but not human readable for debugging.  Pickle is used however between mapper and reducer.
    """
    adj_list = dict()
    # RE to match useful lines
    is_a_row = re.compile('(\d+)\t(\d+)')

    line = stdin.readline()
    while line:
        # Populate adjecency list
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            dst = int(m.group(2))
            if dst in adj_list:
                adj_list[dst].append([src, 1.0])
            else:
                adj_list[dst] = [[src, 1.0]]
        line=stdin.readline()

    # Set initial PR and dump to STDOUT
    pr = 1.0/len(adj_list)
    for k, v in adj_list.items():
        for src in v:
            src[1] = pr
        stdout.write("%s\t%s\n" % (k, json.dumps(v)))


if __name__ == '__main__':
    pre_parse()