import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/')
import numpy as np

def bruteforce(P, Q):
   solQ=[]
   for q in Q:
       md=np.linalg.norm(P[0]-q)
       mi=0
       for i in range(len(P)):
           if np.linalg.norm(np.subtract(P[i],q))<md:
               md=np.linalg.norm(np.subtract(P[i],q))
               mi=i
       solQ.append(mi)   
   return solQ
