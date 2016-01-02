#!/usr/bin/env python2
import re
from sys import stdin, stdout
import json


def mapper():
    """
    Stripes mapper function

    Reads stdin, (emits {w1: {w2_1: n},{w2_2: n}) on stdout
    """
    word_1 = None
    # Dict to store counts before emitting
    n = dict()
    line = stdin.readline()
        while line:
        if len(line) != 0:
            # Make everything lower case
            line = line.lower().strip()
            # Strip non word/whitespace characters
            line = re.sub(r'[^\w\s]', '', line)
            # Replace any whitespace with a single space
            line = re.sub(r'\s+', ' ', line)
            # Loop though words on line
            for word_2 in line.split(' '):
                # Is this a new pair? (following a paragraph)
                if word_1:
                    if word_1 not in n.keys():
                        n[word_1] = dict()
                    if word_2 not in n[word_1].keys():
                        n[word_1][word_2] = 1
                    else:
                        n[word_1][word_2] += 1

                # current word is previous word now
                word_1 = word_2
        else:
            # There was a new paragraph
            word_1 = None
        line = stdin.readline()
    for k, v in n.items():
        stdout.write("%s: %s\n" % (k, json.dumps(v)))

if __name__ == '__main__':
    mapper()
