suhu = int(input("Masukkan suhu reaktor: "))
tekanan = int(input("Masukkan tekanan gas: "))

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"

if suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"

else:
    status = "Reaktor Belum Cukup Panas"

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Suhu reaktor   :", suhu, "derajat")
print("Tekanan gas    :", tekanan, "Bar")
print("Status bahaya  :", status)
print("Status pompa   :", pompa)