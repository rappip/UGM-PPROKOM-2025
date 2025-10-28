import numpy as np

nilai = [
    [85, 80, 90],
    [78, 82, 88],
    [92, 90, 94],
    [70, 68, 72],
    [88, 85, 84],
    [60, 75, 70],
    [95, 92, 98],
    [74, 70, 76],
    [81, 85, 83],
    [69, 72, 70],
    [90, 88, 92],
    [76, 80, 79],
    [84, 86, 90],
    [79, 82, 85],
    [67, 70, 68],
    [91, 94, 93],
    [73, 78, 75],
    [87, 84, 89],
    [65, 68, 70],
    [93, 90, 95],
    [77, 80, 78],
    [82, 84, 88],
    [89, 85, 90],
    [71, 74, 76]
]

# a. Menampilkan seluruh nilai dengan format tertentu menggunakan nested loop
print("a. Data nilai mahasiswa:")
for i in range(len(nilai)):
    tugas, uts, uas = nilai[i]
    if i < 9 :
        print(f"Mahasiswa ke-{i+1}    | Tugas: {tugas} | UTS: {uts} | UAS: {uas}")
    else:
        print(f"Mahasiswa ke-{i+1}   | Tugas: {tugas} | UTS: {uts} | UAS: {uas}")
        
# b. Menggunakan NumPy untuk menampilkan informasi statistik
print("\nb. Informasi statistik nilai mahasiswa:")
nilai_np = np.array(nilai)

# Rata-rata keseluruhan nilai
rata_rata = np.mean(nilai_np)
print(f"Rata-rata keseluruhan nilai: {rata_rata:.2f}")

# Nilai tertinggi
nilai_tertinggi = np.max(nilai_np)
print(f"Nilai tertinggi: {nilai_tertinggi}")

# Nilai terendah
nilai_terendah = np.min(nilai_np)
print(f"Nilai terendah: {nilai_terendah}")