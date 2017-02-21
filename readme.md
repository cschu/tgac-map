### Ordering the TGACv1 CS42 wheat genome assembly scaffolds using a genetic map

#### Data
All data is from https://genomebiology.biomedcentral.com/articles/10.1186/s13059-015-0582-8

1. Marker sequences: W7984 scaffolds from Chapman et al. (2015) http://dx.doi.org/10.5447/IPK/2014/14
2. Genetic map (W7984 x Opata M85) coordinates: Supplementary Dataset S4 from Chapman et al. (2015) http://dx.doi.org/10.5447/IPK/2014/10

#### Correcting the W7984 x Opata M85 map
We corrected the genetic distances between bins by iterating over the bins b and merging bins bi and bi+1 into bi’ if:
- |b(i)-b(i+1)| < 1.6 recombinations (1 recombination represents 0.586 cM on the WGS map)
- b(i)’ did not span more than 2.5 cM [Abraham Korol - pers. comm.].

The map position for each b(i)’ was calculated as the arithmetic mean of all bins merged into it. This is done by the script `chapman_repair.py`.

#### Anchoring TGACv1 scaffolds on W7984 x Opata M85 map
W7984 scaffolds are aligned against TGACv1 scaffolds using megablast.

##### megablast parameters
`blastn -max_target_seqs 1 -evalue 1e-10 -outfmt "7 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen qseq sseq nident mismatch positive gapopen gpas ppos qcovs qcovhsp sstrand qseq sseq"`

#### Create raw map
With `map_blast.py`.

#### Generate scaffold classifications
With `classify_scaffolds.py`.
