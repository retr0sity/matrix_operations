import sys
import matrices

PASS = "\033[92m PASS\033[0m"
FAIL = "\033[91m FAIL\033[0m"

results = []

def test(name, got, expected):
    ok = got == expected
    print(f"[{PASS if ok else FAIL}] {name}")
    if not ok:
        print(f"       Expected: {expected}")
        print(f"       Got:      {got}")
    results.append(ok)

def raises(name, fn):
    try:
        fn()
        print(f"[{FAIL}] {name} (no error raised)")
        results.append(False)
    except ValueError:
        print(f"[{PASS}] {name}")
        results.append(True)


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# add
test("add: 2x2",      matrices.add(A, B),             [[6, 8], [10, 12]])
test("add: zeros",    matrices.add(A, [[0,0],[0,0]]),  A)
test("add: negative", matrices.add([[1,2]], [[-1,-2]]), [[0, 0]])

# subtract
test("subtract: 2x2",  matrices.subtract(B, A),                           [[4, 4], [4, 4]])
test("subtract: self", matrices.subtract(A, A),                            [[0,0],[0,0]])
test("subtract: neg",  matrices.subtract([[1,2],[3,4]], [[5,6],[7,8]]),    [[-4,-4],[-4,-4]])

# multiply
C = [[1, 0], [0, 1]]  # identity
D = [[1, 2, 3], [4, 5, 6]]
E = [[7, 8], [9, 10], [11, 12]]
F = [[1, 2, 3]]
G = [[4], [5], [6]]
test("multiply: identity",   matrices.multiply(A, C), A)
test("multiply: 2x3 × 3x2", matrices.multiply(D, E), [[58, 64], [139, 154]])
test("multiply: dot product",matrices.multiply(F, G), [[32]])

# tensor product
I2 = [[1, 0], [0, 1]]
X2 = [[0, 1], [1, 0]]
test("tensor: scalar ⊗ matrix", matrices.tensor_product([[3]], [[1,2],[3,4]]), [[3,6],[9,12]])
test("tensor: I ⊗ X",           matrices.tensor_product(I2, X2), [[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])

# errors
raises("add: dimension mismatch",      lambda: matrices.add([[1,2]], [[1,2],[3,4]]))
raises("subtract: dimension mismatch", lambda: matrices.subtract([[1,2,3]], [[1,2]]))
raises("multiply: incompatible shapes",lambda: matrices.multiply([[1,2],[3,4]], [[1,2],[3,4],[5,6]]))

passed = sum(results)
total  = len(results)
print(f"\n{'='*40}\n  {passed}/{total} tests passed\n{'='*40}")
sys.exit(0 if passed == total else 1)
