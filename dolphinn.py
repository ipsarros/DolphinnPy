import random, itertools
import numpy as np

class Dolphinn:
     def __init__(self, P, D, K):
         self.P=P
         self.D=D
         self.K=K
         self.h=np.random.multivariate_normal(np.zeros(K), np.eye(K), size=self.D)
         X=np.sign(P.dot(self.h))
         b=np.array([2**j for j in range(self.K)])
         Y=X.dot(b)
         self.cube=dict([])
         for i in range(len(Y)):
             if self.cube.get(int(Y[i]))==None:
                  self.cube[int(Y[i])]=[]
             self.cube[int(Y[i])].append(i)

     def queries(self, Q, M, num_of_probes):
        n=0
        flag=False
        combs=np.ones((num_of_probes,self.K))
        for r in range(self.K+1):
             for c in itertools.combinations(range(self.K),r):
                 for i in c:
                    combs[n,i]=-1
                 n=n+1
                 if n>=num_of_probes:
                    flag=True
                    break
             if flag:
                 break
        #Queries
        #assign keys to queries
        A=np.sign(Q.dot(self.h))
        b=np.array([2**j for j in range(self.K)])
        solQ=[]
        for j in range(len(A)):
           cands=[]
           N=np.multiply(combs,A[j])
           N=N.dot(b)
           for k in N:
              if self.cube.get(int(k))!= None:
                  cands.extend(self.cube[int(k)])             
           if len(cands)>M:
              args=np.argpartition([np.linalg.norm(np.subtract(self.P[i],Q[j])) for i in cands],M)
              sols=[]
              for i in range(M):
                   sols.append(cands[args[i]])
                   
              solQ.append(sols)       
           else:
              solQ.append([-1])
        return solQ
