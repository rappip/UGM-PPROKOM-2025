# Program untuk menerima input nama dan pergantian nama
print("Program Mengelola Nama Teman")
print("=" * 28)

# 1. Meminta user memasukkan 5 nama
nama_teman = []
for i in range(5):
    nama = input(f"Masukkan nama teman ke-{i+1}: ")
    nama_teman.append(nama)

# 2. Menampilkan semua nama dengan indeksnya
print("\nDaftar nama teman:")
for i in range(len(nama_teman)):
    print(f"Indeks {i}: {nama_teman[i]}")

# 3. Menanyakan indeks yang ingin diganti
input_indeks = input("\nMasukkan indeks nama yang ingin diganti (0-4): ").strip()

# Pengecekkan input dengan if-else
if input_indeks in ['0', '1', '2', '3', '4']:
    # Konversi ke integer ketika memenuhi in
    indeks = int(input_indeks)
    
    # 4. Meminta nama pengganti dan melakukan pergantian
    nama_baru = input(f"Masukkan nama baru untuk menggantikan '{nama_teman[indeks]}': ")
    nama_teman[indeks] = nama_baru
    
    # 5. Menampilkan list yang sudah diperbarui
    print("\nDaftar nama teman setelah diperbarui:")
    for i in range(len(nama_teman)):
        print(f"Indeks {i}: {nama_teman[i]}")
else:
    print("Input tidak valid! Harap masukkan angka 0, 1, 2, 3, atau 4.")