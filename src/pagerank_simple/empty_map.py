#!/usr/bin/env python2
from sys import stdin, stdout


def mapper():
    line = stdin.readline()
    while line:
        stdout.write(line)
        line =  stdin.readline()

if __name__ == '__main__':
    mapper()