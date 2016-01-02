#!/usr/bin/env python2
import re
from sys import stdin, stdout


def mapper():
    """
    Pairs mapper function

    Reads stdin, (emits w1 w2 : n=1) on stdout
    """
    previous_word = None
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
            for word in line.split(' '):
                this_word = word
                # Is this a new pair? (following a paragraph)
                if previous_word:
                    # Emit
                    stdout.write("%s %s: %d\n" % (previous_word, this_word, 1))
                # current word is previous word now
                previous_word = this_word
        else:
            # There was a new paragraph
            last_word = None
        line = stdin.readline()

if __name__ == '__main__':
    mapper()
