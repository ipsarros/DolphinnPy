import random, itertools, time
import utils as fr
import numpy as np
import bruteforce as bf
num_of_probes=100

#Preprocessing
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
h=np.random.multivariate_normal(np.zeros(K), np.eye(K), size=D)
X=np.sign(P.dot(h))
b=np.array([2**j for j in range(K)])
Y=X.dot(b)
C=dict([])
for i in range(len(Y)):
    if C.get(int(Y[i]))==None:
        C[int(Y[i])]=[]
    C[int(Y[i])].append(i)

n=0
flag=False
combs=np.ones((num_of_probes,K))
for r in range(K+1):
    for c in itertools.combinations(range(K),r):
        for i in c:
            combs[n,i]=-1
        n=n+1
        if n>=num_of_probes:
           flag=True
           break
    if flag:
      break
toc=time.clock()

print(toc-tic)

tic= time.clock()     
#Queries
#assign keys to queries
A=np.sign(Q.dot(h))
solQ=[]
for j in range(len(A)):
    cands=[]
    N=np.multiply(combs,A[j])
    N=N.dot(b)
    for k in N:
       if C.get(int(k))!= None:
            cands.extend(C[int(k)])             
    if len(cands)>0:
       mi=cands[0]
       md=np.linalg.norm(np.subtract(P[0],Q[j]))
       for i in cands:
          if np.linalg.norm(np.subtract(P[i],Q[j]))<md:
              md=np.linalg.norm(np.subtract(P[i],Q[j]))
              mi=i
       solQ.append(mi)       
    else:
       solQ.append(-1)
toc=time.clock()
print((toc-tic)/len(Q))    
    
#bruteforce
solQQ=bf.bruteforce(P, Q)

# compute accuracy
n=0
for i in range(len(solQ)):
   if solQ[i]==solQQ[i]:
       n=n+1
print(n/len(solQ))







