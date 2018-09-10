#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.split(",")
    # split the line into words
    #words = line.split()
    if len(line) >=25:
        vehicle = line[25]
    else:
        continue
    # increase counters
    #for vehicle in lines:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (vehicle, 1)
