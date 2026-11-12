def hitung_biaya_berat(berat):
    """Menghitung biaya berat paket."""
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000


def hitung_biaya_jarak(jarak):
    """Menghitung biaya jarak pengiriman."""
    if jarak <= 20:
        return 0
    else:
        return 5000


def hitung_ongkir(berat, jarak, anggota):
    """Menghitung ongkir akhir setelah potongan anggota."""
    subtotal = hitung_biaya_berat(berat) + hitung_biaya_jarak(jarak)

    if anggota == "Ya":
        return subtotal * 0.9
    else:
        return subtotal


def tampilkan_struk(nama, berat, jarak, anggota):
    """Menampilkan struk pengiriman satu pelanggan."""

    ongkir = hitung_ongkir(berat, jarak, anggota)

    print(f"{nama:<8}{berat:>3} kg{jarak:>4} km  {anggota:<8}Rp {ongkir:,.0f}")


def main():
    """Menjalankan Program Struk Pengiriman."""

    nama = ["Rina", "Sari", "Tono", "Umar", "Vina"]
    berat = [1, 5, 5, 2, 8]
    jarak = [10, 25, 25, 30, 15]
    anggota = ["Bukan", "Bukan", "Ya", "Ya", "Bukan"]

    print("=" * 45)
    print("STRUK PENGIRIMAN TOKO DARING")
    print("=" * 45)
    print(f"{'Nama':<8}{'Berat':>6}{'Jarak':>7}  {'Anggota':<8}Ongkir")
    print("-" * 45)

    total = 0
    jumlah_anggota = 0

    for i in range(5):
        tampilkan_struk(nama[i], berat[i], jarak[i], anggota[i])

        ongkir = hitung_ongkir(berat[i], jarak[i], anggota[i])
        total = total + ongkir

        if anggota[i] == "Ya":
            jumlah_anggota = jumlah_anggota + 1

    print("=" * 45)
    print("Total pendapatan hari ini: Rp", f"{total:,.0f}")
    print("Jumlah pelanggan anggota:", jumlah_anggota)
    print("=" * 45)


if __name__ == "__main__":
    main()