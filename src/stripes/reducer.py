#!/usr/bin/env python2
import re
from sys import stdin, stdout
import json


def reducer():
    """
    Stripes reducer function

    Reads pairs of words separated by a space and a count and calculates P
    """
    # Empty dict for our output
    n = dict()
    sigma_n = dict()

    # Precompiled regex to match our input
    parse = re.compile('(\w+):(.*)')

    # Read STDIN and get counts
    line = stdin.readline()
    while line:
        # Try and match our line (skip if failed)
        m = parse.match(line)
        if not m:
            continue

        word_1 = m.group(1)
        words = json.loads(m.group(2))

        if word_1 not in n:
            n[word_1] = words
            for i in words.values():
                if word_1 not in sigma_n:
                    sigma_n[word_1] = 0
                sigma_n[word_1] += i
        else:
            for word_2, i in words.items():
                sigma_n[word_1] += i
                if word_2 in n[word_1]:
                    n[word_1][word_2] += i
                else:
                    n[word_1][word_2] = i

        line = stdin.readline()

    # Calculate P
    for word_1 in sorted(n.keys()):
        for word_2, n_word in sorted(n[word_1].items(), key=lambda x: (x[1], x[0]), reverse=True):
            p = n[word_1][word_2] / float(sigma_n[word_1])
            stdout.write("%s %s: %f\n" % (word_1, word_2, p))

if __name__ == '__main__':
    reducer()
