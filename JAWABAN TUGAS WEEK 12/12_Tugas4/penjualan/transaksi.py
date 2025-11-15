# def hitung_total(kode_produk, jumlah):
#     from produk import daftar_produk
    
#     if kode_produk in daftar_produk:
#         harga = daftar_produk[kode_produk]["harga"]
#         total = harga * jumlah
        
#         # Menghitung diskon
#         diskon = 0
#         if total >= 50000:
#             diskon = total * 0.1  # Diskon 10%
#         elif total >= 30000:
#             diskon = total * 0.05  # Diskon 5%
        
#         total_bayar = total - diskon
#         return total, diskon, total_bayar
#     else:
#         return None, None, None


def hitung_total(kode_produk, jumlah):
    from produk import daftar_produk
    
    # Cek apakah kode ada
    if kode_produk not in daftar_produk:
        return None

    harga = daftar_produk[kode_produk]["harga"]
    total = harga * jumlah
    
    # Menghitung diskon
    if total >= 30000:
        diskon = total * 0.05
    elif total >= 50000:
        diskon = total * 0.10
    else:
        diskon = 0

    total_bayar = total - diskon
    return total, diskon, total_bayar