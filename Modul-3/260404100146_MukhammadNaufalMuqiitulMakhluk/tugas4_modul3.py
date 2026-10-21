jumlah_penuh = 0

for i in range(1, 11):
    print("\nData mahasiswa ke-", i)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))
    penghasilan = int(input("Masukkan penghasilan orang tua: Rp"))

    if ipk < 3.00:
        print("Nama:", nama)
        print("Hasil: Tidak memenuhi syarat")
        continue

    if penghasilan <= 3000000:
        if jumlah_penuh < 3:
            status = "Beasiswa Penuh"
            jumlah_penuh = jumlah_penuh + 1
        else:
            status = "Kuota beasiswa penuh sudah habis"

    elif penghasilan <= 5000000:
        status = "Beasiswa Sebagian"

    else:
        status = "Tidak Mendapatkan Beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)

    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print("\nTotal penerima beasiswa penuh:", jumlah_penuh)