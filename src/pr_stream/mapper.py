#!/usr/bin/env python2
from sys import stdin, stdout, stderr
from json import loads, dumps
import re


def mapper():
    is_a_row = re.compile('(\d+)\t(.*)')
    line = stdin.readline()
    while line:
        m = is_a_row.match(line)
        if m:
            src = int(m.group(1))
            if src == 0:
                stdout.write(line)
            else:
                d = loads(m.group(2))
                if d:
                    pr = float(d['pr'])
                    n = int(d['n'])
                    outs = d['out']
                    mm = d['mm'] if 'mm' in d else 0

                    if len(outs) > 0:
                        my_contrib = pr / len(outs)
                        for out in outs:
                            stdout.write("%s\t%s\n" % (out, dumps(dict(
                                    contrib=my_contrib,
                                    n=n,
                                    src=src,
                                    mm=mm
                            ))))
                    else:
                        stdout.write("0\t%s\n" % float(pr/n))
        d = None
        line = stdin.readline()


if __name__ == '__main__':
    mapper()