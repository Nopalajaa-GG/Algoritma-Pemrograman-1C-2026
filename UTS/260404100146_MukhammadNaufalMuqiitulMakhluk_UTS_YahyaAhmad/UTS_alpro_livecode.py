#jenis tiket
regular = 40000
vip = 75000
vvip = 100000

jumlah_tiket = int(input("masukkan jumlah tiket:"))
jenis_tiket = 0
jenis_tiket = input("masukkan jenis tiket:")
total_harga = jumlah_tiket * jenis_tiket
print("total:", total_harga)
if jenis_tiket == regular:
    print("apakah anda mau membeli minuman Rp 10.000 per tiket?")
    jawaban = input("iya")
    jawaban = input("tidak")
    banyak_minuman = input("masukkan banyaknya minuman yang dipesan:")
    
#jenis tiket di atas adalah untuk memberi tahu ada jenis apa saja pada nama tiketnya atau kelas tiketnya 
# lalu untuk memasukkan jumlah tiket kita inputkan
# lalu kita hitung total harga   