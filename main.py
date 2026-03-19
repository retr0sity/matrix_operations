from time import sleep
import matrices


def input_matrix(label, N, M):
    print(f"\n{label}\n")
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            x = int(input(f"  [{i},{j}] = "))
            row.append(x)
        matrix.append(row)
    matrices.print_matrix(matrix, label=f"{label} (entered):")
    return matrix


def main():
    X = 0
    while X != 5:
        X = int(input(
            "Matrix operations\n\n"
            "Please select a function:\n\n"
            "1. Matrix addition\n"
            "2. Matrix subtraction\n"
            "3. Matrix multiplication\n"
            "4. Tensor product\n"
            "5. Exit\n\n"
        ))
        print()

        if X == 1:
            N = int(input("Rows: "))
            M = int(input("Columns: "))
            A = input_matrix("Matrix 1", N, M)
            B = input_matrix("Matrix 2", N, M)
            result = matrices.add(A, B)
            matrices.print_matrix(result, label="Result (A + B):")

        elif X == 2:
            N = int(input("Rows: "))
            M = int(input("Columns: "))
            A = input_matrix("Matrix 1", N, M)
            B = input_matrix("Matrix 2", N, M)
            result = matrices.subtract(A, B)
            matrices.print_matrix(result, label="Result (A - B):")

        elif X == 3:
            print("Matrix A dimensions:")
            N = int(input("  Rows: "))
            M = int(input("  Columns: "))
            A = input_matrix("Matrix A", N, M)
            print("Matrix B dimensions (rows must equal A's columns):")
            P = int(input(f"  Rows (must be {M}): "))
            Q = int(input("  Columns: "))
            B = input_matrix("Matrix B", P, Q)
            try:
                result = matrices.multiply(A, B)
                matrices.print_matrix(result, label="Result (A × B):")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif X == 4:
            print("Matrix A dimensions:")
            N = int(input("  Rows: "))
            M = int(input("  Columns: "))
            A = input_matrix("Matrix A", N, M)
            print("Matrix B dimensions:")
            P = int(input("  Rows: "))
            Q = int(input("  Columns: "))
            B = input_matrix("Matrix B", P, Q)
            result = matrices.tensor_product(A, B)
            matrices.print_matrix(result, label="Result (A ⊗ B):")

        elif X == 5:
            print("Cheerio\n")

        else:
            print("Wrong number! Please enter 1–5.\n")
            sleep(2)


if __name__ == "__main__":
    main()
