#Ioannis Psarros
#
import time
import utils as fr
import numpy as np
import bruteforce as bf
from dolphinn import *
num_of_probes=20   ###########################
M=1   ##########################

#READ FILES
#D1: data dimension, P: dataset
#D2: query dimension, Q: queryset
(D1,P)=fr.fvecs_read("siftsmall/siftsmall_base.fvecs")
(D2,Q)=fr.fvecs_read("siftsmall/siftsmall_query.fvecs")
if D1!=D2:
   raise IOError("Data points and query points are of different dimension")
D=D1

#CHANGE OF ORIGIN
#find the mean of randomly sampled points
m=fr.findmean(P,D,10)
#then consider this mean as the origin
P=fr.isotropize(P,D,m)
Q=fr.isotropize(Q,D,m)
K=int(np.log2(len(P)))-2   ##########################
print "New dimension K=",K

#PREPROCESSING
tic = time.clock()
dol=Dolphinn(P, D, K)
toc=time.clock()
print "Preprocessing time: ",toc-tic

#QUERIES
tic= time.clock()     
#assign keys to queries
solQ=dol.queries(Q, M, num_of_probes)
toc=time.clock()
print "Average query time (Dolphinn): ",(toc-tic)/len(Q)    
    
#BRUTEFORCE
tic= time.clock()     
solQQ=bf.bruteforce(P, Q)
toc=time.clock()
print "Average query time (Bruteforce): ",(toc-tic)/len(Q)  

#COMPUTE ACCURACY: max ratio (found distance)/(NN distance), number of exact NNs found
n=0
mmax=0
for i in range(len(solQ)):
   if mmax<np.linalg.norm(np.subtract(P[solQ[i][0]],Q[i]))/np.linalg.norm(np.subtract(P[solQQ[i]],Q[i])):
       mmax=np.linalg.norm(np.subtract(P[solQ[i][0]],Q[i]))/np.linalg.norm(np.subtract(P[solQQ[i]],Q[i]))
   if solQ[i][0]==solQQ[i]:
       n=n+1

print "Max approximation: ",mmax, ", Accuracy (# of exact NNs): ",n/len(solQ)






