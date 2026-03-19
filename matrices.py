# Matrix operations: add, subtract, multiply, tensor product


def add(A, B):
    _check_same_dimensions(A, B, "addition")
    N, M = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]


def subtract(A, B):
    _check_same_dimensions(A, B, "subtraction")
    N, M = len(A), len(A[0])
    return [[A[i][j] - B[i][j] for j in range(M)] for i in range(N)]


def multiply(A, B):
    # A is (N x M), B must be (M x P), result is (N x P)
    N = len(A)
    M = len(A[0])
    if len(B) != M:
        raise ValueError(
            f"Cannot multiply: A has {M} columns but B has {len(B)} rows."
        )
    P = len(B[0])
    result = [[0] * P for _ in range(N)]
    for i in range(N):
        for j in range(P):
            for k in range(M):
                result[i][j] += A[i][k] * B[k][j]
    return result


def tensor_product(A, B):
    # Each element of A gets replaced by a scaled copy of B
    N, M = len(A), len(A[0])
    P, Q = len(B), len(B[0])
    result = [[0] * (M * Q) for _ in range(N * P)]
    for i in range(N):
        for j in range(M):
            for p in range(P):
                for q in range(Q):
                    result[i * P + p][j * Q + q] = A[i][j] * B[p][q]
    return result


def print_matrix(matrix, label=None):
    if label:
        print(f"\n{label}")
    for row in matrix:
        print("  " + "  ".join(str(x) for x in row))
    print()


def _check_same_dimensions(A, B, operation):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError(
            f"Cannot perform {operation}: "
            f"A is {len(A)}x{len(A[0])} but B is {len(B)}x{len(B[0])}."
        )
