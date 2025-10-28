import numpy as np

# Matriks yang diberikan
A = [[2, 4, 6], [1, 3, 5]]
B = [[1, 1, 1], [2, 2, 2]]

# Mengubah list menjadi array numpy
A_np = np.array(A)
B_np = np.array(B)

# a. Penjumlahan dan pengurangan dengan NumPy
print("a. Operasi penjumlahan dan pengurangan dengan NumPy:")
penjumlahan = A_np + B_np
pengurangan = A_np - B_np

print("Penjumlahan A + B:")
print(penjumlahan)
print("\nPengurangan A - B:")
print(pengurangan)

# b. Perkalian matriks A × Bᵀ
print("\nb. Perkalian matriks A × Bᵀ:")
# Transpose matriks B
B_transpose = B_np.T
print("B transpose:")
print(B_transpose)

# Perkalian matriks A dengan B transpose
perkalian = np.dot(A_np, B_transpose)
print("\nHasil perkalian A × Bᵀ:")
print(perkalian)