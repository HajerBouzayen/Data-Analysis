import numpy as np

def random_mat (N) :
    M = 5 + 5 * np.random.randn(N,2)
    M[:,1]=2*M[:,0]

    return M
def build_m(M, N, n=2):
    
    for i in range(n+1):
        
        indexL = np.random.randint(N-1)
        indexC = np.random.randint(1)
        M[indexL , indexC] = np.nan
        
    return M

def nettoyage(M) :
    print("**Fonction de nettoyage**")
    mediancolonne=np.nanmedian(M,axis=0)
    print("mediancolonne",mediancolonne)
    for l in range(M.shape[0]):
        for c in range(M.shape[1]):
            if np.isnan(M[l,c]):
                M[l,c]=mediancolonne[c]
    return M

