# a. Menggunakan nested list comprehension untuk membuat matriks identitas 4x4
print("a. Matriks identitas 4x4 dengan nested list comprehension:")
n = 4
matriks_identitas = [
    [1 if i == j else 0 for j in range(n)] 
    for i in range(n)]
for baris in matriks_identitas:
    print(baris)

# b. Menambahkan variabel input n untuk menentukan ukuran matriks identitas
print("\nb. Matriks identitas dengan ukuran yang ditentukan pengguna:")
n = int(input("Masukkan ukuran matriks identitas: "))
matriks_identitas_custom = [
    [1 if i == j else 0 for j in range(n)] 
    for i in range(n)]
print(f"Matriks identitas {n}x{n}:")
for baris in matriks_identitas_custom:
    print(baris)