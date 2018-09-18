import time
import utils as fr
import numpy as np
import bruteforce as bf
from dolphinn import *
num_of_probes=20
M=1
#Preprocessing
#D1: data dimension, P: dataset
#D2: query dimension, Q: queryset
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
#initialize hyperplane lsh
tic = time.clock()
dol=Dolphinn(P, D, K)
toc=time.clock()

print(toc-tic)

tic= time.clock()     
#Queries
#assign keys to queries
solQ=dol.queries(Q, M, num_of_probes)
toc=time.clock()
print((toc-tic)/len(Q))    
    
#bruteforce
solQQ=bf.bruteforce(P, Q)

# compute accuracy
n=0
mmax=0
for i in range(len(solQ)):
   if mmax<np.linalg.norm(np.subtract(P[solQ[i][0]],Q[i]))/np.linalg.norm(np.subtract(P[solQQ[i]],Q[i])):
       mmax=np.linalg.norm(np.subtract(P[solQ[i][0]],Q[i]))/np.linalg.norm(np.subtract(P[solQQ[i]],Q[i]))
   if solQ[i][0]==solQQ[i]:
       n=n+1

print("Max approximation: ",mmax, ", Accuracy (exact NN): ",n/len(solQ))






