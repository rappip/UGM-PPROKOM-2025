import aritmatika

# Fungsi untuk memastikan input adalah angka
def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.\n")

# Menerima input dari pengguna
angka1 = input_angka("Masukkan angka pertama: ")
angka2 = input_angka("Masukkan angka kedua: ")

# Menampilkan hasil operasi
print(f"\nHasil Penjumlahan: {aritmatika.penjumlahan(angka1, angka2)}")
print(f"Hasil Pengurangan: {aritmatika.pengurangan(angka1, angka2)}")
print(f"Hasil Perkalian: {aritmatika.perkalian(angka1, angka2)}")
print(f"Hasil Pembagian: {aritmatika.pembagian(angka1, angka2)}")
print(f"Hasil Modulo: {aritmatika.modulo(angka1, angka2)}")
print(f"Hasil Pangkat: {aritmatika.pangkat(angka1, angka2)}")