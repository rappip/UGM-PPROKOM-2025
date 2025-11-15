import produk
import transaksi


def input_kode_produk():
    from produk import daftar_produk

    while True:
        kode = input("Masukkan kode produk yang dibeli: ")

        if not kode.isdigit():
            print("Kode produk tidak valid! Harus berupa angka.\n")
            produk.tampilkan_produk()
            continue

        if kode not in daftar_produk:
            print("Kode produk tidak ditemukan!\n")
            produk.tampilkan_produk()
            continue

        return kode


def input_jumlah():
    while True:
        jumlah = input("Masukkan jumlah yang dibeli: ")

        if jumlah.isdigit():
            return int(jumlah)
        else:
            print("Input tidak valid! Masukkan angka.")


def main():
    while True:   
        produk.tampilkan_produk()

        kode_produk = input_kode_produk()
        jumlah = input_jumlah()

        hasil = transaksi.hitung_total(kode_produk, jumlah)

        if hasil is None:
            print("Kode produk tidak valid!\n")
            continue

        total, diskon, total_bayar = hasil

        # Tampilkan Struk
        print("\n=== STRUK PEMBAYARAN ===")
        nama_produk = produk.daftar_produk[kode_produk]["nama"]
        print(f"Produk      : {nama_produk}")
        print(f"Jumlah      : {jumlah}")
        print(f"Total       : Rp {total}")
        print(f"Diskon      : Rp {diskon}")
        print(f"Total Bayar : Rp {total_bayar}")
        print("=========================")

        
        while True:
            lanjut = input("\nIngin lanjut belanja? (y/n): ").lower()

            if lanjut == 'y':
                break            # kembali ke loop utama → belanja lagi
            elif lanjut == 'n':
                print("Terima kasih telah berbelanja!")
                exit()
            else:
                print("Berikan input berupa y atau n!")


if __name__ == "__main__":
    main()