# Tugas 1 Algoritma dan Pemrograman

## SOAL 1

### Tabel Fungsi Soal 1

| Nama Fungsi | Parameter | Mengembalikan Nilai (Ya/Tidak) | Tugas yang Dikerjakan |
|---|---|---|---|
| hitung_nilai | tugas, uts, uas | Ya (Non-void) | Menghitung nilai akhir dengan bobot tugas 30%, UTS 30%, dan UAS 40% |
| nilai_huruf | nilai | Ya (Non-void) | Mengonversi nilai akhir menjadi nilai huruf (A, B, C, D, E) |
| kelulusan | huruf | Ya (Non-void) | Menentukan status LULUS atau TIDAK LULUS berdasarkan nilai huruf (minimal C) |
| tampilkan_nilai | nama, tugas, uts, uas | Tidak (Void) | Mencetak nama, nilai akhir, nilai huruf, dan status satu mahasiswa |

Fungsi `main()` menyiapkan data lima mahasiswa, memanggil `tampilkan_nilai` untuk tiap mahasiswa, lalu mencetak rata-rata kelas dan jumlah mahasiswa yang lulus.

### Perhitungan Manual

**1. Andi** (Tugas: 80, UTS: 70, UAS: 90)

- Nilai akhir: (80 x 0,30) + (70 x 0,30) + (90 x 0,40) = 24 + 21 + 36 = 81,00
- Nilai huruf: 81 berada pada rentang 70 sampai < 85, maka nilai hurufnya B.
- Verifikasi: keluaran program menghasilkan nilai akhir 81.0 dengan nilai huruf B (sesuai).

**2. Dimas** (Tugas: 75, UTS: 80, UAS: 65)

- Nilai akhir: (75 x 0,30) + (80 x 0,30) + (65 x 0,40) = 22,5 + 24 + 26 = 72,50
- Nilai huruf: 72,5 berada pada rentang 70 sampai < 85, maka nilai hurufnya B.
- Verifikasi: keluaran program menghasilkan nilai akhir 72.5 dengan nilai huruf B (sesuai).

### Tambahan Fitur

Menambahkan satu fungsi non-void baru, misalnya `cari_tertinggi(nama, daftar_nilai)`, untuk membandingkan nilai akhir semua mahasiswa dan mengembalikan nama mahasiswa dengan nilai terbesar. Fungsi `main` ikut diubah: nilai akhir tiap mahasiswa disimpan ke sebuah list, lalu fungsi baru dipanggil setelah perulangan dan hasilnya dicetak.

### Fungsi yang Tidak Perlu Disentuh

`hitung_nilai`, `nilai_huruf`, `kelulusan`, dan `tampilkan_nilai`. Masing-masing hanya mengerjakan satu tugas spesifik dan tidak berurusan dengan perbandingan antar mahasiswa, jadi bisa dipakai kembali tanpa mengubah logikanya.

---

## SOAL 2

### Tabel Fungsi Soal 2

| Nama Fungsi | Parameter | Mengembalikan Nilai (Ya/Tidak) | Tugas yang Dikerjakan |
|---|---|---|---|
| hitung_biaya_berat | berat | Ya (Non-void) | Menghitung biaya berat paket (Rp10.000 untuk <= 2 kg, tambah Rp4.000 per kg berikutnya) |
| hitung_biaya_jarak | jarak | Ya (Non-void) | Menentukan biaya jarak (Rp0 jika <= 20 km, Rp5.000 jika > 20 km) |
| hitung_ongkir | berat, jarak, anggota | Ya (Non-void) | Menjumlahkan biaya berat dan jarak, lalu memberi potongan 10% jika anggota |
| tampilkan_struk | nama, berat, jarak, anggota | Tidak (Void) | Mencetak struk satu pelanggan |

Fungsi `main()` menyiapkan data lima pesanan, memanggil `tampilkan_struk` untuk tiap pelanggan, lalu mencetak total pendapatan dan jumlah pelanggan anggota.

### Perhitungan Manual Ongkir Akhir

**Sari** (berat: 5 kg, jarak: 25 km, anggota: bukan)

- Biaya berat: 10.000 + (5 - 2) x 4.000 = 22.000
- Biaya jarak: 25 > 20, maka Rp5.000
- Subtotal: 22.000 + 5.000 = 27.000 (tidak ada potongan karena bukan anggota)
- Ongkir akhir: Rp27.000 (program menghasilkan yang sama)

**Tono** (berat: 5 kg, jarak: 25 km, anggota: ya)

- Biaya berat: Rp22.000, biaya jarak: Rp5.000
- Subtotal: 22.000 + 5.000 = 27.000
- Potongan anggota (10%): 0,10 x 27.000 = 2.700
- Ongkir akhir: 27.000 - 2.700 = Rp24.300 (program menghasilkan angka yang sama)

**Umar** (berat: 2 kg, jarak: 30 km, anggota: ya)

- Biaya berat: 2 kg = Rp10.000
- Biaya jarak: 30 > 20, maka Rp5.000
- Subtotal: 10.000 + 5.000 = 15.000
- Potongan anggota (10%): 1.500
- Ongkir akhir: 15.000 - 1.500 = Rp13.500 (program menghasilkan angka yang sama)

### Bagian Kode yang Harus Diubah

Jika batas jarak menjadi 15 km dan biaya tambahan jarak menjadi Rp7.000, yang diubah hanya fungsi `hitung_biaya_jarak(jarak)`:

```python
def hitung_biaya_jarak(jarak):
    """Menghitung biaya jarak pengiriman."""
    if jarak <= 15:      # diubah dari 20 menjadi 15
        return 0
    else:
        return 7000      # diubah dari 5000 menjadi 7000
```

Karena aturan jarak sudah dipisah ke fungsi tersendiri, cukup satu fungsi yang diubah tanpa menyentuh `main` atau fungsi lain. Pemisahan tugas ini membuat kode lebih mudah diubah.
