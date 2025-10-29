import numpy as np  

# Función para leer la matriz de coeficientes A (3x3)
def leerMatriz():
    print("\nIngresa los valores de la matriz de coeficientes A (3x3):")
    matriz = []  # Aquí se guardan las filas de la matriz

    for fila_idx in range(3):
        fila = input(f"Fila {fila_idx + 1} (3 números separados por espacio): ").strip().split()

        # Validar que se ingresen 3 valores
        if len(fila) != 3:
            print("Debes ingresar exactamente 3 números por fila.")
            return leerMatriz()

        # Convertir a tipo float y manejar errores
        try:
            fila = [float(valor) for valor in fila]
        except ValueError:
            print("Solo se permiten números. Intenta de nuevo.")
            return leerMatriz()

        matriz.append(fila)

    # Convertir la lista a un arreglo NumPy 3x3
    return np.array(matriz)

# Función para leer el vector de demandas b (3x1)
def leerVector():
    print("\nIngresa los valores del vector de demanda b (3x1):")
    entrada = input("Tres valores separados por espacio: ").strip().split()

    # Validar cantidad de valores
    if len(entrada) != 3:
        print("Debes ingresar exactamente 3 números.")
        return leerVector()

    # Convertir los valores a flotantes
    try:
        vector_demanda = [float(valor) for valor in entrada]
    except ValueError:
        print("Solo se permiten números. Intenta de nuevo.")
        return leerVector()

    return np.array(vector_demanda)

# Función para calcular la solución del sistema Ax = b
def resolverSistema(matriz_A, vector_b):
    determinante = np.linalg.det(matriz_A)

    print("\n============================")
    print("Matriz A:")
    print(matriz_A)
    print(f"\nVector b: {vector_b}")
    print(f"Determinante det(A) = {determinante:.6f}")

    # Verificar si la matriz es invertible
    if abs(determinante) < 1e-12:
        print("\nLa matriz A NO es invertible (determinante ≈ 0).")
        print("Generando matriz alternativa A' (diagonal ajustada)...")

        matrizAlternativa = matriz_A.copy()
        np.fill_diagonal(matrizAlternativa, matrizAlternativa.diagonal() - 1)
        determinante_alternativo = np.linalg.det(matrizAlternativa)

        print("\nMatriz A' (ajustada):")
        print(matrizAlternativa)
        print(f"Determinante det(A') = {determinante_alternativo:.6f}")

        # Si la matriz ajustada tampoco es invertible, se detiene
        if abs(determinante_alternativo) < 1e-12:
            print("\nA' tampoco es invertible. No se puede resolver el sistema.")
            return
        else:
            inversaAlternativa = np.linalg.inv(matrizAlternativa)
            vector_solucion = inversaAlternativa.dot(vector_b)

            print("\nInversa de A' (A'^{-1}):")
            print(np.round(inversaAlternativa, 6))
            print("\nSolución x (usando A'):")
            print(np.round(vector_solucion, 6))

    else:
        # Calcular inversa y solución si A sí es invertible
        inversaA = np.linalg.inv(matriz_A)
        vector_solucion = inversaA.dot(vector_b)

        print("\nInversa de A (A^{-1}):")
        print(np.round(inversaA, 6))
        print("\nSolución x:")
        print(np.round(vector_solucion, 6))

    print("============================\n")

# Función principal (menú y control del programa)
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
        opcion = input("Opción: ").strip()

        if opcion == "1":
            matriz_A = leerMatriz()
            vector_b = leerVector()
            resolverSistema(matriz_A, vector_b)

        elif opcion == "2":
            # Ejemplo automático
            matriz_A = np.array([
                [-2.0, 1.0, 1.0],
                [1.0, -2.0, 1.0],
                [1.0, 1.0, -2.0]
            ])
            vector_b = np.array([50.0, 80.0, 120.0])
            resolverSistema(matriz_A, vector_b)

        elif opcion == "0":
            print("\nCerrando el programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
