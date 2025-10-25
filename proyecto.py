import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ------------------------------------------------------------
# PRESENTACIÓN DEL GRUPO
integrantes = [
    "Christopher De la Cruz",
    "Rubén Darío",
    "Gustavo Bances",
    "Romulo García"
]

print("========= PROYECTO ÁLGEBRA LINEAL =========")
print("Optimización de una red usando matrices")
print("\nIntegrantes del grupo:")
for i in integrantes:
    print(" -", i)
print("==========================================\n")

# ------------------------------------------------------------
# FUNCIÓN PARA PROCESAR UNA MATRIZ Y UN VECTOR b
def resolver_sistema(A, b):
    detA = np.linalg.det(A)
    print("\nMatriz A:\n", A)
    print("Vector b:", b)
    print("Determinante:", detA)

    if abs(detA) < 1e-12:
        print("\nA NO es invertible. Usando matriz alternativa A'...")
        A_alt = A.copy()
        np.fill_diagonal(A_alt, A_alt.diagonal() - 1)  # solo bajamos en 1 la diagonal

        detA_alt = np.linalg.det(A_alt)
        print("\nNueva matriz A':\n", A_alt)
        print("Determinante de A':", detA_alt)

        A_inv = np.linalg.inv(A_alt)
        x = A_inv.dot(b)
        print("\nSolución x usando A'·x = b:\n", x)

        return A_alt, x
    else:
        print("\nA es invertible.")
        A_inv = np.linalg.inv(A)
        x = A_inv.dot(b)
        print("\nSolución x = A^{-1}·b:\n", x)
        return A, x

# ------------------------------------------------------------
# MATRIZ A ORIGINAL
A_inicial = np.array([
    [-2.0, 1.0, 1.0],
    [1.0, -2.0, 1.0],
    [1.0, 1.0, -2.0]
])

# ------------------------------------------------------------
# SIMULACIÓN DE VARIOS ESCENARIOS
resultados = []

print("Puedes simular varios escenarios de demanda.")
print("Cuando quieras terminar, escribe: 0 0 0")

while True:
    print("\nIngresa las demandas del vector b (3 nodos):")
    entrada = input("Ej: 50 80 120 → ")
    
    try:
        valores = list(map(float, entrada.split()))
        if len(valores) != 3:
            print("Debes ingresar exactamente 3 valores.")
            continue
    except:
        print("Formato no válido.")
        continue

    # salir al ingresar 0 0 0
    if valores == [0.0, 0.0, 0.0]:
        break

    b = np.array(valores)
    A_usada, x = resolver_sistema(A_inicial, b)
    resultados.append((b, x))

print("Ejecucion terminada.")