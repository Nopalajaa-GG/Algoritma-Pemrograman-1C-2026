jarak_rumah_ke_saudara_dimas = 100
konsumsi_bensin = 40
harga_bensin_per_liter = 10000
sisa_bensin = 1.5

jarak_yang_ditempuh_dimas = jarak_rumah_ke_saudara_dimas * 2
total_kebutuhan_bensin_dimas = jarak_yang_ditempuh_dimas / konsumsi_bensin
jumlah_bensin_yang_harus_dibeli_dimas = total_kebutuhan_bensin_dimas - sisa_bensin
total_biaya_bensin_dimas = jumlah_bensin_yang_harus_dibeli_dimas * harga_bensin_per_liter

print("jarak yang ditempuh dimas pulang pergi adalah:", jarak_yang_ditempuh_dimas, "km")
print("total kebutuhan bensin dimas untuk pulang pergi adalah:", total_kebutuhan_bensin_dimas, "liter")
print("jumlah bensin yang harus dibeli dimas untuk pulang pergi dimas adalah:", jumlah_bensin_yang_harus_dibeli_dimas, "liter")
print("total biaya untuk beli bensin pulang pergi dimas adalah:", total_biaya_bensin_dimas, "Rp")