#!/usr/bin/env python2
from sys import stdin, stdout
import re
import json


def pre_parse(teleport):
    """
    Reads original file on stdin, calculates initial PR as 1/n and outputs adjeceny list with each inbound PR stored
    for every node in the format:

    node    {'m': [n, teleport], 's': [[N1, PR1, OL1], [N2, PR2, OL2], ... [Nn, PRn, OLn]]}
    (Value is JSON serialised)

    Although not space/bandwidth efficient, it allows each node to be processed independently and means we can safely use
    the TextInputFormat class from Hadoop.  Using Pickle(2) would be much more efficient but not human readable for
    debugging.  Pickle is used however between mapper and reducer.
    """

    # Empty adjency list
    adj_list_in = dict()
    links_out = dict()
    # RE to match useful lines
    is_a_row = re.compile('(\d+)\t(\d+)')

    # Read original file
    line = stdin.readline()
    while line:
        # Populate adjecency list
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            dst = int(m.group(2))
            # Set the PRs to 1.0 to pre-allocate space for a float and number of links to 0
            if dst in adj_list_in:
                adj_list_in[dst].append([src, 1.0, 0])
            else:
                adj_list_in[dst] = [[src, 1.0, 0]]
        line=stdin.readline()

    # Set initial PR and dump to STDOUT
    n = len(adj_list_in)
    pr = 1.0/n

    # Output each row (metadata and source nodes with PR)
    for k, v in adj_list_in.items():
        for src in v:
            src[1] = pr
            # Add out outbound link count
            if src[0] not in links_out:
                links_out[src[0]] = 1
            else:
                links_out[src[0]] += 1

    for k, v in adj_list_in.items():
        for src in v:
            src[2] = links_out[src[0]]

        stdout.write("%s\t%s\n" % (k, json.dumps(dict(
            p=pr,
            m=[n, teleport],    # Metadata
            s=v                 # Inbound nodes and PRs
        ))))


if __name__ == '__main__':
    pre_parse(teleport=0.25)
