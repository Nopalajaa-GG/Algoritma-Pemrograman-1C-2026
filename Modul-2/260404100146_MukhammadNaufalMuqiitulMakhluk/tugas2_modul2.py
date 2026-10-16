total = int(input("Masukkan total belanja: Rp "))

if total % 100000 == 0:
    bayar = 0
    diskon = total
    print("Mendapat diskon 100% (Gratis)")

elif total % 50000 == 0:
    diskon = 0.5 * total
    bayar = total - diskon
    print("Mendapat diskon 50%")

elif total % 10000 == 0:
    diskon = 0.2 * total
    bayar = total - diskon
    print("Mendapat diskon 20%")

elif total >= 200000:
    diskon = 0.1 * total
    bayar = total - diskon
    print("Mendapat diskon 10%")

else:
    bayar = total
    print("Tidak mendapat diskon")

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal : Rp", total)
print("Anda mendapat diskon : Rp", diskon)
print("Total yang dibayar : Rp", bayar)
print("Status poin        :", poin)