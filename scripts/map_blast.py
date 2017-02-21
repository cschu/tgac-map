#!/usr/bin/env python
from __future__ import division
import sys
import csv
from collections import Counter, defaultdict


fn = sys.argv[1]
with open(fn) as fi:
    # there are two .map-files in group-tg/reference/wheat-geneticbin-map/
    gmap = {line.split('\t')[0]: tuple(line.strip().split('\t')[1:3]) for line in fi}

cmap = Counter()
dmap = defaultdict(Counter)

fi = sys.stdin
reader = csv.reader(fi, delimiter='\t')
for row in reader:
    # print row
    if not row[0].startswith('#'):
        evalue = float(row[10])
        if evalue > 1e-5:
            continue
        alen = float(row[3])
        qlen = float(row[12])
        if alen < 1000: #200 or alen / qlen < 0.75:
            continue
        pid = float(row[2])
        if pid < 98.5: #85.0:
            continue
        cmap[tuple(row[:2])] += 1
        dmap[row[0]][row[1]] += 1

# make sure to only use markers that align to one scaffold
for k in dmap:
    if len(dmap[k]) == 1:
        cmap[(k, dmap[k].keys()[0])] = dmap[k].values()[0]


for k in sorted(cmap):
    chr_, bin_ = gmap.get(k[0], (None, None))
    if chr_ and bin_:
        print '\t'.join(map(str, [k[0], k[1], cmap[k], chr_, bin_]))
