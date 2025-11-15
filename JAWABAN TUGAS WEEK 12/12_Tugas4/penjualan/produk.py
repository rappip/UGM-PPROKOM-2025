# Daftar produk dan harga
daftar_produk = {
    "1": {"nama": "Buku", "harga": 15000},
    "2": {"nama": "Pensil", "harga": 3000},
    "3": {"nama": "Pulpen", "harga": 5000},
    "4": {"nama": "Penggaris", "harga": 4000},
    "5": {"nama": "Tipe-X", "harga": 7000}
}

def tampilkan_produk():
    print("\n=== Daftar Produk ===")
    for kode, produk in daftar_produk.items():
        print(f"{kode}. {produk['nama']} - Rp {produk['harga']}")