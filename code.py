import copy

import numpy
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

    return P, din, dout

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

    G = alpha * P + (1 - alpha) * (E / n)
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

    n = len(A)
    P, din, dout = GetMat(A)
    G = GoogleMat(P, alpha, v)

    # I = np.identity(n)
    #
    # Pfinal = numpy.delete(
    #     np.append([np.ones(n)], I - np.transpose(P), axis=0),
    #     n, 0)
    #
    # vect = np.ones(n)
    # vect[1:n] = 0

    """
    This function must return the left eigen vector of G associatied with the only eigen value equal to 1.0
    """

    return "Some work has to be done."

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
    P, din, dout = GetMat(A)

    G = GoogleMat(P, alpha, v)
    Gt = np.transpose(G)
    dprev = np.ones(n) * np.inf

    eps = 10 ** -9
    while error(dprev, din) > eps:
        dprev = din
        din = np.dot(Gt, din)

    return din / np.sum(din)
