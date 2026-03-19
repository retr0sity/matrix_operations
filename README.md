# matrix_operations
 
A small Python module for matrix operations — addition, subtraction, multiplication, and tensor product.
 
## Files
 
- `matrices.py` — the module, import this in your own scripts
- `main.py` — interactive menu for manual use
- `test_matrices.py` — run this to verify everything works
 
## Usage
 
```python
import matrices
 
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
 
matrices.add(A, B)
matrices.subtract(A, B)
matrices.multiply(A, B)
matrices.tensor_product(A, B)
```
 
## Running the tests
 
```
python test_matrices.py
```
 
## Requirements
 
Python 3. No external libraries.
