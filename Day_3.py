"""
NumPy Assignment - Multidimensional Arrays
--------------------------------------------
Task:
1. Create multidimensional arrays
2. Use index numbers to access values and perform mathematical operations
3. Apply at least 15 NumPy methods
"""

import numpy as np

# -------------------------------------------------
# STEP 1: Create multidimensional arrays
# -------------------------------------------------
arr_2d = np.array([[10, 20, 30, 40],
                    [50, 60, 70, 80],
                    [90, 100, 110, 120]])

arr_3d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]],
                    [[9, 10], [11, 12]]])

print("=" * 60)
print("2D Array:")
print("=" * 60)
print(arr_2d)

print("\n" + "=" * 60)
print("3D Array:")
print("=" * 60)
print(arr_3d)

# -------------------------------------------------
# STEP 2: Index-based access and math operations
# -------------------------------------------------
print("\n" + "=" * 60)
print("Indexing examples")
print("=" * 60)
print("Element at row 0, col 2 (2D array):", arr_2d[0, 2])
print("Element at row 2, col 3 (2D array):", arr_2d[2, 3])
print("Entire row 1 (2D array):", arr_2d[1, :])
print("Entire column 2 (2D array):", arr_2d[:, 2])
print("Element in 3D array [1,1,0]:", arr_3d[1, 1, 0])
print("Slice of 3D array [0:2, 1, :]:", arr_3d[0:2, 1, :])

print("\n" + "=" * 60)
print("Mathematical operations using indexed values")
print("=" * 60)
sum_result = arr_2d[0, 0] + arr_2d[1, 1]
diff_result = arr_2d[2, 3] - arr_2d[0, 1]
prod_result = arr_2d[1, 2] * arr_2d[0, 3]
div_result = arr_2d[2, 2] / arr_2d[0, 0]
print(f"arr_2d[0,0] + arr_2d[1,1] = {sum_result}")
print(f"arr_2d[2,3] - arr_2d[0,1] = {diff_result}")
print(f"arr_2d[1,2] * arr_2d[0,3] = {prod_result}")
print(f"arr_2d[2,2] / arr_2d[0,0] = {div_result}")

# -------------------------------------------------
# STEP 3: Apply at least 15 NumPy methods
# -------------------------------------------------

print("\n" + "=" * 60)
print("METHOD 1: shape -> dimensions of array")
print("=" * 60)
print("arr_2d shape:", arr_2d.shape)
print("arr_3d shape:", arr_3d.shape)

print("\n" + "=" * 60)
print("METHOD 2: ndim -> number of dimensions")
print("=" * 60)
print("arr_2d ndim:", arr_2d.ndim)
print("arr_3d ndim:", arr_3d.ndim)

print("\n" + "=" * 60)
print("METHOD 3: size -> total number of elements")
print("=" * 60)
print("arr_2d size:", arr_2d.size)

print("\n" + "=" * 60)
print("METHOD 4: reshape() -> change array shape")
print("=" * 60)
reshaped = arr_2d.reshape(4, 3)
print(reshaped)

print("\n" + "=" * 60)
print("METHOD 5: flatten() -> convert to 1D array")
print("=" * 60)
print(arr_2d.flatten())

print("\n" + "=" * 60)
print("METHOD 6: transpose() -> swap rows and columns")
print("=" * 60)
print(arr_2d.transpose())

print("\n" + "=" * 60)
print("METHOD 7: sum() -> sum of all elements")
print("=" * 60)
print("Total sum:", arr_2d.sum())
print("Column-wise sum:", arr_2d.sum(axis=0))
print("Row-wise sum:", arr_2d.sum(axis=1))

print("\n" + "=" * 60)
print("METHOD 8: mean() -> average value")
print("=" * 60)
print("Mean:", arr_2d.mean())

print("\n" + "=" * 60)
print("METHOD 9: max() and argmax() -> maximum value and its index")
print("=" * 60)
print("Max value:", arr_2d.max())
print("Index of max (flattened):", arr_2d.argmax())

print("\n" + "=" * 60)
print("METHOD 10: min() and argmin() -> minimum value and its index")
print("=" * 60)
print("Min value:", arr_2d.min())
print("Index of min (flattened):", arr_2d.argmin())

print("\n" + "=" * 60)
print("METHOD 11: std() -> standard deviation")
print("=" * 60)
print("Standard deviation:", arr_2d.std())

print("\n" + "=" * 60)
print("METHOD 12: sqrt() -> square root of each element")
print("=" * 60)
print(np.sqrt(arr_2d))

print("\n" + "=" * 60)
print("METHOD 13: sort() -> sort array elements")
print("=" * 60)
unsorted_arr = np.array([[40, 10, 30], [90, 20, 60]])
print("Before sorting:\n", unsorted_arr)
print("After sorting:\n", np.sort(unsorted_arr))

print("\n" + "=" * 60)
print("METHOD 14: concatenate() -> join two arrays")
print("=" * 60)
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr_a, arr_b), axis=0))

print("\n" + "=" * 60)
print("METHOD 15: where() -> conditional selection")
print("=" * 60)
result = np.where(arr_2d > 60, "High", "Low")
print(result)

print("\n" + "=" * 60)
print("METHOD 16: dot() -> matrix multiplication")
print("=" * 60)
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
print(np.dot(mat_a, mat_b))

print("\n" + "=" * 60)
print("METHOD 17: linspace() -> evenly spaced values")
print("=" * 60)
print(np.linspace(0, 100, 5))

print("\n" + "=" * 60)
print("METHOD 18: arange() -> array with a range of values")
print("=" * 60)
print(np.arange(0, 20, 2))

print("\nAll NumPy operations completed successfully!")
