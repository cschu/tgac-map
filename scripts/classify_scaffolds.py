#!/usr/bin/env python
import sys
import csv

from collections import Counter

classes = {'unique': 'class1', 'conflict': 'class4', 'ambiguous': 'class2', 'homoeolog': 'class3'}

scaffolds = {}
reader = csv.reader(sys.stdin, delimiter='\t')
for row in reader:
    if row[1] not in scaffolds:
        scaffolds[row[1]] = Counter()
    scaffolds[row[1]][(row[3], row[4])] += 1

#with open('uniquely_placed_scaffolds.tsv', 'wb') as uniq_out:
uniquely_placed = list()
multi_bins = list()
conflicts = list()
homeologs = list()
for scaffold in scaffolds:
    if (len(scaffolds[scaffold])) == 1:
        uniquely_placed.append(scaffold)
        class_ = 'unique'
    else:
        chromosomes = set(item[0][0] for item in scaffolds[scaffold])
        genomes = set(item[0][1] for item in scaffolds[scaffold])
        assert chromosomes
        assert genomes
        if len(chromosomes) > 1:
            conflicts.append(scaffold)
            class_ = 'conflict'
        elif len(genomes) == 1:
            # bins = set(item[1] for item in scaffolds[scaffold])
            multi_bins.append(scaffold)
            class_ = 'ambiguous'
        elif len(genomes) > 1:
            homeologs.append(scaffold)
            class_ = 'homoeolog'

    print '\t'.join([scaffold, ';'.join(['%s:%s' % bin_ for bin_ in sorted(scaffolds[scaffold])]), class_ + ':' + classes.get(class_, 'NONE')])



sys.exit(0)
ordered = []
for scaffold in scaffolds:
    if len(scaffolds[scaffold]) == 1:
        ordered.append((scaffold,) + list(scaffolds[scaffold])[0])

for scaffold in sorted(ordered, key=lambda x:(x[1][1], int(x[1][0]), float(x[2]))):
    print '\t'.join(map(str, scaffold))
