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
        din[i] = np.sum(A[:, i])
        if dout[i] != 0: P[i] = A[i] / dout[i]
        else: P[i] = A[i]

    return P

print(GetMat(np.array([
    [1.0, 2.0],
    [3.0, 4.0]
]))[0])

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

    P, din ,dout = GetMat(A)
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
    n = len(A)
    P = GetMat(A)
    x = v
    G = GoogleMat(P, alpha, v) # google mat is correct
    Gt = G.transpose()
    prev = np.ones(n) * np.inf

    eps = 10 ** -9
    while True:
        prev = x
        x = np.dot(Gt, x)
        print(x)

    return x #Normalize
