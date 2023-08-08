from math import isclose

import numpy as np

def multMM(matrices):
    resultado = matrices[0]

    for i in range(1, len(matrices)):
        m2 = matrices[i]
        temp_resultado = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]

        for i in range(len(resultado)):
            for j in range(len(m2[0])):
                for k in range(len(resultado[0])):
                    temp_resultado[i][j] += resultado[i][k] * m2[k][j]

        resultado = temp_resultado

    return resultado

    return resultado

def multMV(m, v):
    resultado = [0, 0, 0, 0]
    for i in range(len(m)):
        for j in range(len(m[0])):
            resultado[i] += m[i][j] * v[j]

    return resultado

def bcCoords(A, B, C, P):
    BCP = abs((P[0] * C[1] + C[0] * B[1] + B[0] * P[1]) - (P[1] * C[0] + C[1] * B[0] + B[1] * P[0]))
    CAP = abs((A[0] * C[1] + C[0] * P[1] + P[0] * A[1]) - (A[1] * C[0] + C[1] * P[0] + P[1] * A[0]))
    ABP = abs((A[0] * B[1] + B[0] * P[1] + P[0] * A[1]) - (A[1] * B[0] + B[1] * P[0] + P[1] * A[0]))
    
    ABC = abs((A[0] * B[1] + B[0] * C[1] + C[0] * A[1]) - (A[1] * B[0] + B[1] * C[0] + C[1] * A[0]))

    """ BCP = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    CAP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])
    #ABP = (A[1] - B[1]) * (P[0] - C[0]) + (B[0] - A[0]) * (P[1] - C[1])
    
    ABC = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1]) """

    if ABC == 0:
        return None

    u = BCP / ABC
    v = CAP / ABC
    w = ABP / ABC
    #w = 1 - u - v

    if (0 <= u <= 1) and (0 <= v <= 1) and (0 <= w <= 1) and isclose(u + v + w, 1.0):
        return (u, v, w)
    else:
        return None

def invertMatrix(matrix):
    """ a, b, c, d = matrix[0]
    e, f, g, h = matrix[1]
    i, j, k, l = matrix[2]
    m, n, o, p = matrix[3]

    det = a * (f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)) - \
          b * (e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)) + \
          c * (e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)) - \
          d * (e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m))
    
    if det == 0:
        return -1
    else:
        inversa = [
            [(f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n)) / det,
             -(b * (k * p - l * o) - c * (j * p - l * n) + d * (j * o - k * n)) / det,
             (b * (f * p - h * o) - c * (e * p - g * o) + d * (e * o - f * n)) / det,
             -(b * (f * l - h * k) - c * (e * l - g * j) + d * (e * k - f * j)) / det],

            [-(e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m)) / det,
             (a * (k * p - l * o) - c * (i * p - l * m) + d * (i * o - k * m)) / det,
             -(a * (f * p - h * o) - c * (e * p - g * o) + d * (e * o - f * m)) / det,
             (a * (f * l - h * k) - c * (e * l - g * i) + d * (e * k - f * i)) / det],

            [(e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m)) / det,
             -(a * (j * p - l * n) - b * (i * p - l * m) + d * (i * n - j * m)) / det,
             (a * (f * p - h * n) - b * (e * p - g * n) + d * (e * h - f * m)) / det,
             -(a * (f * l - h * j) - b * (e * l - g * i) + d * (e * h - f * i)) / det],

            [-(e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m)) / det,
             (a * (j * o - k * n) - b * (i * o - k * m) + c * (i * n - j * m)) / det,
             -(a * (f * o - g * n) - b * (e * o - g * m) + c * (e * n - f * m)) / det,
             (a * (f * k - g * j) - b * (e * k - g * i) + c * (e * j - f * i)) / det]
        ]
        return inversa """
    return np.linalg.inv(matrix)

#prueba = [[1, 1, 0, 0], [0, -1, -2, 0], [0, 0, 1, -1], [0, 0, 0, 1]]
#print(invertMatrix(prueba))