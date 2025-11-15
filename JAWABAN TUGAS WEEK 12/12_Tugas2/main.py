import konversi_suhu

def show_menu():
    print("Program Konversi Suhu")
    print("Pilih jenis konversi:")
    print("[1]. Celcius ke Fahrenheit")
    print("[2]. Celcius ke Kelvin")
    print("[3]. Fahrenheit ke Celcius")
    print("[4]. Fahrenheit ke Kelvin")
    print("[5]. Kelvin ke Celcius")
    print("[6]. Kelvin ke Fahrenheit")
    print("[7]. Keluar")

    pilihan = int(input("Masukkan pilihan (1-7): "))
    # suhu = float(input("Masukkan suhu yang akan dikonversi: "))

    if pilihan == 1:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.celcius_to_fahrenheit(suhu)
            print(f"{suhu}°C = {hasil}°F")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 2:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.celcius_to_kelvin(suhu)
            print(f"{suhu}°C = {hasil}K")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 3:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.fahrenheit_to_celcius(suhu)
            print(f"{suhu}°F = {hasil}°C")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 4:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.fahrenheit_to_kelvin(suhu)
            print(f"{suhu}°F = {hasil}K")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 5:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.kelvin_to_celcius(suhu)
            print(f"{suhu}K = {hasil}°C")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 6:
        try:
            suhu = float(input("Masukkan suhu yang akan dikonversi: "))
            hasil = konversi_suhu.kelvin_to_fahrenheit(suhu)
            print(f"{suhu}K = {hasil}°F")
        except ValueError:
            print("Input harus berupa bilangan!\n")
    elif pilihan == 7:
        print("Terima kasih telah menggunakan kalkulator ini!")
        exit()
    else:
        print("Pilihan tidak valid!\n")

while True:
    show_menu()