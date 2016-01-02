#!/usr/bin/env python2
from sys import stdin, stdout, stderr, exit
import re
import json


def pre_parse():
    adj_list = dict()
    # RE to match useful lines
    is_a_row = re.compile('(\d+)\t(\d+)')

    line = stdin.readline()
    while line:
        # Populate adjecency list
        m = is_a_row.match(line)
        if m:
            src = m.group(1)
            dst = m.group(2)
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