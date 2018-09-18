DolphinnPy

Python 2.7

Numpy is required: numpy.org
for instance: pip install numpy

DolphinnPy provides with a simple, yet efficient method for the problem of computing an (approximate) nearest neighbor in high dimensions. The algorithm is based on https://arxiv.org/abs/1612.07405, where we show linear space and sublinear query for a specific setting of parameters.

First, N points are randomly mapped to keys in {0,1}^K, for K<=logN, by making use of the Hypeplane LSH family. Then, for a given query, candidate nearest neighbors are the ones within a small hamming radius with respect to their keys. Our approach resembles the multi-probe LSH approach but it differs on how the list of candidates is computed.

Files:

main.py: reads files, builds data structure, executes queries. dolphinn.py: data structure constructor, queries method. utils.py: various useful functions. bruteforce.py: linear scan for validation purposes.

Hardcoded parameters (in main.py):

K: new dimension - key bit length. 
num_of_probes: how many buckets are allowed to be visited. 
M: how many candidate points are allowed to be examined.

Dataset, queryset files paths are in the script: in fvecs format.
Requires input from http://corpus-texmex.irisa.fr/

How to run: python main.py

Preprocesses dataset, then runs Dolphinn and brute-force search on all queries.
Prints K, preprocessing and average-query times.
Prints multiplicative approximation, number of exact answers.
