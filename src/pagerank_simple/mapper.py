#!/usr/bin/env python2
from sys import stdin, stdout, stderr
import re
import json
import pickle


def mapper():
    t = None
    n = None
    line_errors = 0

    parse_line = re.compile('(\d+)\t(.*)')
    line = stdin.readline()
    while line:
        m = parse_line.match(line)
        if m:
            node = int(m.group(1))
            data = json.loads(m.group(2))
            # Do we have our metadata (load once)
            if not n:
                n = data['m'][0]
            if not t:
                t = data['m'][1]
                t_by_n = float(t) / n

            # Calculate our new PR
            data['p'] = t_by_n + (1 - t) * \
                sum(
                    i[1] / i[2] for i in data['s']
                )

            # Emit (with value pickled for size/efficiency)
            stdout.write("%s\t%s\n" %(node, json.dumps(data, 2)))
        else:
            line_errors += 1

        line = stdin.readline()
    # stderr.write("%d line errors\n" % (line_errors,))


if __name__ == '__main__':
    mapper()