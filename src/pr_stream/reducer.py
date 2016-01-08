#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from json import loads, dumps
import re


def reducer(df):
    is_a_row = re.compile('(\d+)\t(.*)')
    mm = None
    n = None
    pr = dict()
    adj_in = dict()

    line = stdin.readline()
    while line:
        m = is_a_row.match(line)
        if m:
            dst = int(m.group(1))
            if dst == 0:
                # Pass missing mass to missing_reducer
                stdout.write(line)
            else:
                d = loads(m.group(2))
                if d:
                    if not n:
                        n = d['n']
                    src = d['src']
                    contrib = d['contrib']
                    # Only set mm once
                    if not mm and 'mm' in d:
                        mm = d['mm']
                    # Add each contribution
                    if dst not in pr:
                        pr[dst] = 0.0
                        adj_in[dst] = []
                    pr[dst] += contrib
                    adj_in[dst].append(src)
        d = None
        line = stdin.readline()

    # If there was no mm then 0
    if not mm:
        mm = 0
    stderr.write("Reducer with Missing Mass: %s\n" % mm)

    # Make outlinks adj list from inlinks
    adj_out = dict()
    for dst, srcs in adj_in.items():
        for src in srcs:
            if src not in adj_out:
                adj_out[src] = []
            adj_out[src].append(dst)
        # In case of no outlinks
        if dst not in adj_out:
            adj_out[dst] = []

    # Calculate PRs
    for dst in pr:
        pr[dst] = (1 - df)/n + df * (pr[dst] + (mm/n))

    # Emit
    for src, dsts in adj_in.items():
        stdout.write("%s\t%s\n" % (src, dumps(dict(
            pr=pr[src],
            n=n,
            out=adj_out[src]
        ))))

if __name__ == '__main__':
    reducer(df=0.85)