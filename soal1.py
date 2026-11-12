def hitung_nilai(tugas, uts, uas):
    """Menghitung nilai akhir mahasiswa."""
    return tugas * 0.3 + uts * 0.3 + uas * 0.4


def nilai_huruf(nilai):
    """Menentukan nilai huruf mahasiswa."""
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


def kelulusan(huruf):
    "Menentukan status Kelulusan Mahasiswa."

    if huruf == "A" or huruf == "B" or huruf == "C":
        return "LULUS"
    else:
        return "TIDAK LULUS"


def tampilkan_nilai(nama, tugas, uts, uas):
    """Menampilkan hasil nilai mahasiswa."""

    nilai = hitung_nilai(tugas, uts, uas)
    huruf = nilai_huruf(nilai)
    status = kelulusan(huruf)

    print(nama, nilai, huruf, status)


def main():
    """Menjalankan Program Rekapitulasi Nilai."""

    nama = ["Andi", "Bunga", "Citra", "Dimas", "Eka"]
    tugas = [80, 90, 60, 75, 30]
    uts = [70, 85, 45, 80, 40]
    uas = [90, 88, 50, 65, 35]

    print("="* 35)
    print("REKAP NILAI MAHASISWA")
    print("="* 35)

    total = 0
    jumlah_lulus = 0

    for i in range(5):
        tampilkan_nilai(nama[i], tugas[i], uts[i], uas[i])

        nilai = hitung_nilai(tugas[i], uts[i], uas[i])
        total = total + nilai

        huruf = nilai_huruf(nilai)

        if kelulusan(huruf) == "LULUS":
            jumlah_lulus = jumlah_lulus + 1

    rata_rata = total // 5

    print("=" * 45)
    print("Rata-rata kelas:", rata_rata)
    print("Jumlah mahasiswa lulus:", jumlah_lulus)
    print("=" * 45)


if __name__ == "__main__" :
    main()