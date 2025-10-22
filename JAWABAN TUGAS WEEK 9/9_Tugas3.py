# Program untuk mengelola array integer
from array import array

print("Program Mengelola Array Integer")
print("=" * 31)

# 1. Mengimpor modul array (sudah dilakukan di atas)

# 2. Membuat array integer dengan 5 nilai
arr_int = array('i', [10, 20, 30, 40, 50])

# 3. Menampilkan array dan panjangnya
print("\nArray integer:", arr_int)
print("Panjang array:", len(arr_int))

# 4. Menghitung jumlah total elemen
total = 0  # Awalan variabel total dengan 0
for angka in arr_int:  # Perulangan untuk setiap elemen dalam array
    total = total + angka  # Menambahkan setiap elemen ke total
print("\nJumlah total semua elemen:", total)

# 5. Menghitung dan menampilkan nilai rata-rata
rata_rata = total / len(arr_int)
print("Nilai rata-rata:", rata_rata)