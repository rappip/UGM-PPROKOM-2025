A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

# a. Tampilkan semua elemen pada lapisan pertama saja (menggunakan slicing)
print("a. Elemen pada lapisan pertama:")
lapisan_pertama = A[0]  # Mengambil lapisan pertama
print(lapisan_pertama)

# b. Tampilkan semua elemen kolom terakhir dari setiap baris dan lapisan
print("\nb. Elemen kolom terakhir dari setiap baris dan lapisan:")
for i in range(len(A)):  # Loop untuk setiap lapisan
    for j in range(len(A[i])):  # Loop untuk setiap baris dalam lapisan
        # Mengambil elemen terakhir dari baris j pada lapisan i
        elemen_terakhir = A[i][j][2]
        print(f"Lapisan {i}, Baris {j}, Elemen terakhir: {elemen_terakhir}")