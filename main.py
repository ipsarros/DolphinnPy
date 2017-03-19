import time
import utils as fr
import numpy as np
import bruteforce as bf
from dolphinn import *
num_of_probes=100

#read input
(D1,P)=fr.fvecs_read("siftsmall/siftsmall_base.fvecs")
(D2,Q)=fr.fvecs_read("siftsmall/siftsmall_query.fvecs")
#(D1,P)=fr.fvecs_read("sift/sift_base.fvecs")
#(D2,Q)=fr.fvecs_read("sift/sift_query.fvecs")
if D1!=D2:
   raise IOError("Data points and query points are of different dimension")
D=D1
m=fr.findmean(P,D,10)
P=fr.isotropize(P,D,m)
Q=fr.isotropize(Q,D,m)
K=int(np.log2(len(P)))-2
print("K=",K)
#Initialize dolphinn
tic = time.clock()
dol=Dolphinn(P, D, K)
toc=time.clock()
print(toc-tic)
#Queries
tic= time.clock()     
solQ=dol.queries(Q, num_of_probes)
toc=time.clock()
print((toc-tic)/len(Q))    
#Bruteforce
solQQ=bf.bruteforce(P, Q)
#Compute accuracy-Percentage of correct exact NN
n=0
for i in range(len(solQ)):
   if solQ[i]==solQQ[i]:
       n=n+1
print(n/len(solQ))







