jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 100

for i in range(1, 11):
    print("\nData Mahasiswa ke-", i)

    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A = jumlah_A + 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B = jumlah_B + 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C = jumlah_C + 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D = jumlah_D + 1
    else:
        kategori = "E"
        jumlah_E = jumlah_E + 1

    total_nilai = total_nilai + nilai_akhir

    if nilai_akhir > nilai_tertinggi or i == 1:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah or i == 1:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\n--- Hasil Nilai Mahasiswa ---")
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", nilai_akhir, 2)
    print("Kategori    :", kategori)

rata_rata = total_nilai / 10

print("\n===== REKAP NILAI SELURUH MAHASISWA =====")
print("Jumlah mahasiswa kategori A:", jumlah_A)
print("Jumlah mahasiswa kategori B:", jumlah_B)
print("Jumlah mahasiswa kategori C:", jumlah_C)
print("Jumlah mahasiswa kategori D:", jumlah_D)
print("Jumlah mahasiswa kategori E:", jumlah_E)

print("\nNilai akhir tertinggi:", nilai_tertinggi, 2)
print("Nama mahasiswa       :", nama_tertinggi)

print("\nNilai akhir terendah :", nilai_terendah, 2)
print("Nama mahasiswa       :", nama_terendah)

print("\nRata-rata nilai akhir:", rata_rata, 2)