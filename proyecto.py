import numpy as np

def leer_matriz():
    print("\nIngresa los valores de la matriz A (3x3):")
    A = []
    for i in range(3):
        fila = input(f"Fila {i+1} (3 números separados por espacio): ").strip().split()
        if len(fila) != 3:
            print("Debes ingresar exactamente 3 números por fila.")
            return leer_matriz()
        try:
            fila = [float(x) for x in fila]
        except ValueError:
            print("Solo se permiten números. Intenta de nuevo.")
            return leer_matriz()
        A.append(fila)
    return np.array(A)

def leer_vector():
    print("\nIngresa el vector b (3x1):")
    fila = input("Tres valores separados por espacio: ").strip().split()
    if len(fila) != 3:
        print("Debes ingresar exactamente 3 números.")
        return leer_vector()
    try:
        b = [float(x) for x in fila]
    except ValueError:
        print("Solo se permiten números. Intenta de nuevo.")
        return leer_vector()
    return np.array(b)

def calcular(A, b):
    detA = np.linalg.det(A)
    print("\n============================")
    print("Matriz A:")
    print(A)
    print(f"\nVector b: {b}")
    print(f"Determinante det(A) = {detA:.6f}")

    if abs(detA) < 1e-12:
        print("\nLa matriz A NO es invertible (determinante ≈ 0).")
        print("Generando matriz alternativa A' (diagonal ajustada)...")
        A_alt = A.copy()
        np.fill_diagonal(A_alt, A_alt.diagonal() - 1)
        det_alt = np.linalg.det(A_alt)
        print("\nMatriz A':")
        print(A_alt)
        print(f"Determinante det(A') = {det_alt:.6f}")

        if abs(det_alt) < 1e-12:
            print("\nA' tampoco es invertible. No se puede resolver el sistema.")
            return
        else:
            Ainv = np.linalg.inv(A_alt)
            x = Ainv.dot(b)
            print("\nA'^{-1}:")
            print(np.round(Ainv, 6))
            print("\nSolución x (usando A'):")
            print(np.round(x, 6))
    else:
        Ainv = np.linalg.inv(A)
        x = Ainv.dot(b)
        print("\nA^{-1}:")
        print(np.round(Ainv, 6))
        print("\nSolución x:")
        print(np.round(x, 6))

    print("============================\n")

def main():
    print("===============================================")
    print("  PROYECTO: Optimización de un Sistema de Redes")
    print("===============================================")
    print("Integrantes:")
    print(" - Christopher De la Cruz")
    print(" - Rubén Darío")
    print(" - Romulo García")
    print(" - Gustavo Bances")
    print("===============================================")

    while True:
        print("\nElige una opción:")
        print("1. Ingresar matriz y vector manualmente")
        print("2. Usar ejemplo automático (del proyecto original)")
        print("0. Salir")
        op = input("→ Opción: ").strip()

        if op == "1":
            A = leer_matriz()
            b = leer_vector()
            calcular(A, b)
        elif op == "2":
            A = np.array([
                [-2.0, 1.0, 1.0],
                [1.0, -2.0, 1.0],
                [1.0, 1.0, -2.0]
            ])
            b = np.array([50.0, 80.0, 120.0])
            calcular(A, b)
        elif op == "0":
            print("\nPrograma finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
