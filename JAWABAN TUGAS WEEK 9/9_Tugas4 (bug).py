from array import array

list_buah = ["Apel", "Mangga", "Jeruk"]
list_buah.append("Anggur")
list_buah.pop("Mangga")
print("List Buah:", list_buah)

arr_nilai = array('f', [85.5, 92.0, 78.5, 90.0])
arr_nilai.append(87.0)
nilai_pertama = arr_nilai[0]
print("Nilai pertama adalah: " + nilai_pertama)
arr_nilai[2] = "Delapan Puluh"
print("Array Nilai:", arr__nilai)