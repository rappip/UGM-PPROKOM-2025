# Nama dan NIM
print("Nama: Rafif Nanda Pramuditya")
print("NIM: 25/550734/SV/26472")

# Fungsi penjumlahan
def penjumlahan(a, b):
    return a + b

# Fungsi pengurangan
def pengurangan(a, b):
    return a - b

# Fungsi perkalian
def perkalian(a, b):
    return a * b

# Fungsi pembagian
def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak dapat dibagi dengan nol"

# Fungsi perpangkatan
def perpangkatan(a, b):
    return a ** b

# Fungsi akar kuadrat
def akar_kuadrat(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Tidak dapat menghitung akar dari bilangan negatif"

# Fungsi untuk menampilkan menu
def show_menu():
    print("\nMenu Kalkulator:")
    print("[1] Penjumlahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Perpangkatan")
    print("[6] Akar Kuadrat")
    print("[7] Keluar")
    
    menu = input("Pilih menu: ")
    
    if menu == "1":
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
            hasil = penjumlahan(a, b)
            print(f"Hasil penjumlahan: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "2":
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
            hasil = pengurangan(a, b)
            print(f"Hasil pengurangan: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "3":
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
            hasil = perkalian(a, b)
            print(f"Hasil perkalian: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "4":
        try:
            a = float(input("Masukkan bilangan pertama: "))
            b = float(input("Masukkan bilangan kedua: "))
            hasil = pembagian(a, b)
            print(f"Hasil pembagian: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "5":
        try:
            a = float(input("Masukkan bilangan yang akan dipangkatkan: "))
            b = float(input("Masukkan pangkat: "))
            hasil = perpangkatan(a, b)
            print(f"Hasil perpangkatan: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "6":
        try:
            a = float(input("Masukkan bilangan yang akan diakarkan: "))
            hasil = akar_kuadrat(a)
            print(f"Hasil akar kuadrat: {hasil}")
        except ValueError:
            print("Error: Input harus berupa bilangan!")
    elif menu == "7":
        print("Terima kasih telah menggunakan kalkulator ini!")
        exit()
    else:
        print("Menu tidak tersedia")

while True:
    show_menu()