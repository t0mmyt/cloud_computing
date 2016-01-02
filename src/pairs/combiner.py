#!/usr/bin/env python2
import re
from sys import stdin, stdout


def combiner():
    """
    Pairs combiner function

    Reads pairs of words separated by a space and a count and aggregates counts
    """
    # Empty dict for out output
    output = dict()
    # Precompiled regex to match our input
    parse = re.compile('(\w+) (\w+): (\d+)')
    line = stdin.readline()
    while line:
        # Try and match our line (skip if failed)
        m = parse.match(line)
        if m:
            word_1 = m.group(1)
            word_2 = m.group(2)
            count = int(m.group(3))
            words = "%s %s" % (word_1, word_2)
            # Add the count
            if output.has_key(words):
                output[words] += count
            else:
                output[words] = count
        line = stdin.readline()

    # stdout the sorted list
    for this in sorted(output.items(), key=lambda x: (x[1], x[0]), reverse=True):
        stdout.write("%s: %d\n" % this)

if __name__ == '__main__':
    combiner()
