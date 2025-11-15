import data_mhs

while True:
    print("\nMenu:")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Keluar")
    
    pilihan = input("Masukkan pilihan (1-3): ")
    
    if pilihan == "1":
        nama = str(input("Masukkan nama mahasiswa: "))
        nim = str(input("Masukkan NIM mahasiswa: "))
        data_mhs.tambah_data(nama, nim)
    elif pilihan == "2":
        data_mhs.tampilkan_data()
    elif pilihan == "3":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")