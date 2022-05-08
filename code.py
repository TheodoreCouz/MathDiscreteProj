from statistics import pvariance
import numpy as np



def GetMat(A):
    """
    Input:
    A = adjacency matrix of a graph

    Output:
    P = transition probabilities matrix
    din = vector containing the indegrees
    dout = vector containing the outdegrees
    """
    n = len(A)
    dout = np.ones(n)
    din = np.ones(n)
    P = A

    for i in range(n):
        dout[i] = np.sum(A[i])
        din[i] = np.sum(A[:,i])
        if dout[i] != 0: P[i] = A[i] / dout[i]
        else: P[i] = A[i]

    return P

def GoogleMat(P, alpha, v):
    """
    Input:
    P = transition probabilities matrix
    alpha = coeff to build the Google matrix

    Output:
    G = Google matrix built from P and alpha
    """
    n = len(P)
    E = np.ones(n) * np.transpose(v)
    G = alpha * P + (1 - alpha) * (E)
    return G

def pageRankLinear(A, alpha, v):
    """
    Input : Une matrice d’adjacence A d’un graphe dirigé,
    pondéré et régulier G, un vecteur de personnalisation v,
    ainsi qu’un paramètre de téléportation α compris entre
    0 et 1 (0.9 par défaut et pour les résultats à présenter).
    Toutes ces valeurs sont nonnégatives.

    – Output : Un vecteur x contenant les scores
    d’importance des noeuds ordonnés dans
    le même ordre que la matrice d’adjacence.
    """

    # A is the adjacency matrix

    P = GetMat(A) # <matrice de probabilités de transisition>
    n = len(A)
    I = np.identity(n)
    alphaP = alpha * P
    firstSide = np.transpose(I - alphaP)
    secondSide = (1 - alpha) * v
    return np.linalg.solve(firstSide, secondSide)

def error(a, b):
    """
    Input:
    a = vector
    b = vector

    Output:
    Max = the maximum error between a[i] and b[i]
    """
    Max = 0
    if len(a) != len(b): raise IndexError('a and b must be equally sized')
    for i in range(len(a)):
        Max = max(abs(a[i] - b[i]), Max)
    return Max

def pageRankPower(A, alpha, v):
    """
    – Input : Une matrice d’adjacence A d’un graphe dirigé,
    pondéré et régulier G, un vecteur de personnalisation v,
    ainsi qu’un paramètre de téléportation α compris entre 0
    et 1, α ∈]0,1[ (0.9 par défaut et pour les résultats à présenter).

    – Output : Un vecteur x contenant les scores
    d’importance des noeuds ordonnés dans
    le même ordre que la matrice d’adjacence.
    """
    # A is the adjacency matrix

    n = len(A)
    P = GetMat(A) # <matrice de probabilités de transisition>
    x = v
    G = GoogleMat(P, alpha, v) # <Google matrix>
    Gt = G.transpose()
    prev = np.ones(n) * np.inf

    eps = 10 ** -9
    # this condition will be false when the result will have converged
    # According to the instructions, we must write the 3 first iterations only
    # The condition must be changed for the report
    while error(x, prev) > eps: 
        prev = x
        x = np.dot(Gt, x)

    return x #Normalize

"""
@param:
mPath: path to the file containing the adjacency matrix of the graph we're working on
vPath: path to the file containing the personalization vector we must use to compute the pagerank

@result:
AdjMat: adjacency matrix translated in order to be usable in python
pVect: personalization vector translated in order to be usable in python
"""
def readFiles(mPath, vPath):
    AdjMat= []
    with open(mPath, 'r') as file:  # reads adjacency matrix
        for line in file.read().split("\n"):
            if len(line) <= 10: break
            AdjMat.append([])
            for elem in line.strip().split(","):
                AdjMat[-1].append(float(elem))
        file.close()

    pVect = []
    with open(vPath, 'r') as file: # reads perso vector
        for line in file.read().split("\n"):
            if len(line) <= 10: break
            for elem in line.strip().split(","):
                pVect.append(float(elem))
        file.close()

    return np.array(AdjMat), np.array(pVect)

def main(): # main function 

    AdjMat, pVect = readFiles("adjacencyMat.csv", "vectorPerso.csv")
    alpha = 0.9 # default value given in the instructions

    Linear = pageRankLinear(AdjMat, alpha, pVect)
    print(f"Result from Linear Method:\n{Linear}")

    Power = pageRankPower(AdjMat, alpha, pVect)
    print(f"Result from Power Method:\n{Power}")

    # Notice that the two functions must return the same pageRankVector
    # If not, there is a problem somewhere


#-------Executed Instructions-------#

main()
