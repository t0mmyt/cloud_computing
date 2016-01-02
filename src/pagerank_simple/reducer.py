#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from copy import deepcopy
import re
import json
import pickle


def reducer():
    line_errors = 0
    page_ranks = dict()
    adj_graphs = dict()

    parse_line = re.compile('(\d+)\t(.*)')

    line = stdin.readline()
    while line:
        m = parse_line.match(line)
        if m:
            node = int(m.group(1))
            data = json.loads(m.group(2))

            adj_graphs[node] = data
            page_ranks[node] = data['p']
        else:
            line_errors += 1
        line = stdin.readline()

    # stderr.write("%d line errors\n" % (line_errors,))

    # Update our huge graph with the new PRs
    for node, data in adj_graphs.items():
        for this in data['s']:
            # Some nodes never received a vote, give them some blank data
            if this[0] not in page_ranks:
                page_ranks[this[0]] = 0
                adj_graphs[this[0]] = deepcopy(adj_graphs[adj_graphs.keys()[0]])
                adj_graphs[this[0]].update(dict(p=0, s=[]))
            this[1] = page_ranks[this[0]]

    # Output sorted by PR
    for node, pr in sorted(page_ranks.items(), key=lambda x: x[1], reverse=True):
        stdout.write( "%d\t%s\n" % (node, json.dumps(adj_graphs[node])))


if __name__ == '__main__':
    reducer()