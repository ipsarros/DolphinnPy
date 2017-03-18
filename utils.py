import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/')
import numpy as np


def fvecs_read(filename, c_contiguous=True):
    fv = np.fromfile(filename, dtype=np.float32)
    if fv.size == 0:
        return np.zeros((0, 0))
    dim = fv.view(np.int32)[0]
    assert dim > 0
    fv = fv.reshape(-1, 1 + dim)
    if not all(fv.view(np.int32)[:, 0] == dim):
        raise IOError("Non-uniform vector sizes in " + filename)
    fv = fv[:, 1:]
    if c_contiguous:
        fv = fv.copy()
    return (dim,fv)
def findmean(P, D, r):
    if len(P)>1000:
        s=int(len(P)/r)
    else:
        s=len(P)
    #randomly sample pointset
    J=np.random.choice(range(len(P)),s)
    m=np.zeros(D)
    for i in J:
        m=np.add(m,P[i])
    m=np.divide(m,s)
    return m
def isotropize(P, D, m):
     #find mean in order to isotropize
    for i in range(len(P)):
        P[i]=np.subtract(P[i],m)
    return P

