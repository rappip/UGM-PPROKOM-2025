# List untuk menyimpan data mahasiswa
data_mahasiswa = []

def tambah_data(nama, nim):
    data_mahasiswa.append({"nama": nama, "nim": nim})
    print(f"Data mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan")

def tampilkan_data():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa")
    else:
        print("\nDaftar Mahasiswa:\n")
        for i, mhs in enumerate(data_mahasiswa, 1):
            print(f"{i}. Nama: {mhs['nama']}, NIM: {mhs['nim']}")