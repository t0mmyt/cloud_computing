#!/usr/bin/env python2
import re
from sys import stdin, stdout
import json


def reducer():
    """
    Pairs reducer function

    Reads pairs of words separated by a space and a count and calculates P
    """
    # Empty dict for our output
    n = dict()
    sigma_n = dict()

    # Precompiled regex to match our input
    parse = re.compile('(\w+)\s+(\w+):\s+(\d+)')

    # Read STDIN and get counts
    line = stdin.readline()
    while line:
        # Try and match our line (skip if failed)
        m = parse.match(line)
        if m:
            word_1 = m.group(1)
            word_2 = m.group(2)
            count = int(m.group(3))
            # Add our count to d
            if word_1 not in n.keys():
                n[word_1] = dict()
                sigma_n[word_1] = 0
            if word_2 not in n[word_1].keys():
                n[word_1][word_2] = count
            else:
                n[word_1][word_2] += count
            sigma_n[word_1] += count

        line = stdin.readline()

    # Calculate P
    for word_1 in sorted(n.keys()):
        for word_2, n_word in sorted(n[word_1].items(), key=lambda x: (x[1], x[0]), reverse=True):
            p = n[word_1][word_2] / float(sigma_n[word_1])
            stdout.write("%s %s: %f\n" % (word_1, word_2, p))

if __name__ == '__main__':
    reducer()
