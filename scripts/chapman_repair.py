#!/usr/bin/env python
from __future__ import division
import sys
import csv

RECOMB_SIZE = 0.586
MAX_RECOMB_PER_BIN = 1.6
MAX_BIN_SIZE = 2.5

reader = csv.reader(sys.stdin, delimiter='\t')

# bin = [(chr, cM), (chr, cM), ..., (chr, cM)]
def print_bin(bin_, bin_index):
    new_coord = sum(item[1] for item in bin_) / len(bin_)
    for i, item in enumerate(bin_):
        print '\t'.join(map(str, [item[0], item[1], new_coord]))
    """

        if i == 0:
            print '->',
        print bin_index, item[0], item[1],
        if i > 0:
            print item[1] - bin_[i-1][1], (item[1] - bin_[i-1][1]) / RECOMB_SIZE,
        print
    print '=>', bin_index, bin_[-1][0],
    """


current_bin = []
bin_index = 0
for row in reader:
    chr_, cM = row[0], float(row[1])
    if not current_bin or current_bin[-1][0] != chr_:
        if current_bin:
            print_bin(current_bin, bin_index)
            bin_index += 1
        current_bin = [(chr_, cM)]
    else:
        d_cM = cM - current_bin[-1][1]
        n_recomb = d_cM / RECOMB_SIZE
        if n_recomb < MAX_RECOMB_PER_BIN:
            if cM - current_bin[0][1] < MAX_BIN_SIZE:
                current_bin.append((chr_, cM))
                continue
        # new bin
        print_bin(current_bin, bin_index)
        bin_index += 1
        current_bin = [(chr_, cM)]

print_bin(current_bin, bin_index)
