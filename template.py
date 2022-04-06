import numpy
import numpy as np

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

    n = len(A)
    I = np.identity(n)
    dout = np.ones(n)
    din = np.ones(n)
    P = A

    for i in range(n):
        dout[i] = np.sum(A[i])
        din[i] = np.sum(A[:, i])
        P[i] = A[i] / dout[i]

    Pfinal = numpy.delete(
        np.append([np.ones(n)], I-np.transpose(P), axis=0),
        n, 0)

    vect = np.ones(n)
    vect[1:n] = 0

    return np.linalg.solve(Pfinal, vect)

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

    return



print(pageRankLinear(np.array([
    [0.0, 2.0, 0.0],
    [0.0, 0.0, 2.0],
    [1.0, 1.0, 0.0]
]), 1.0, 1.0))
