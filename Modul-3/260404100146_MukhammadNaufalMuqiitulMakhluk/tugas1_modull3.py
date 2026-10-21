jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukkan jarak penumpang (km), 0 untuk selesai: "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid, silakan masukkan ulang!")
        continue

    jumlah_penumpang = jumlah_penumpang + 1
    total_jarak = total_jarak + jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Selamat! Penumpang mendapat diskon 50%")

    total_pendapatan = total_pendapatan + tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif yang harus dibayar: Rp", int(tarif))

print("=== HASIL AKHIR ===")
print("Jumlah penumpang:", jumlah_penumpang)
print("Total pendapatan: Rp", int(total_pendapatan))

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jarak terjauh:", jarak_terjauh, "km")
    print("Rata-rata jarak:", round(rata_rata, 2), "km")
else:
    print("Jarak terjauh: 0 km")
    print("Rata-rata jarak: 0 km")
