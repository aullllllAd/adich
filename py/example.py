print("| ====================== |")
print("|           AULL         |")
print("| ====================== |")
print("| ES JERUK      RP.10000 |")
print("| ES TEH        RP.5000  |")
print("| JUS BUAH      RP.15000 |")
print("| ES KOPI SUSU  RP.11000 |")
print("| ICE LEMON TEA RP.12000 |")
print("| ====================== |")

no_minuman  = int(input("masukan no makanan yang ingin kamu pesan : "))
jml_porsi   = int(input("masukan jumlah pesanan kamu : "))

if no_makanan == 1:
    total_minuman = jml_porsi * 10000
    print(f"ES JERUK, {jml_porsi} porsi Rp.{total_minuman}")
    minuman = "ES JERUK"  
elif no_makanan == 2:
    total_minuman = jml_porsi * 5000
    print(f"ES TEH, {jml_porsi} porsi Rp.{total_minuman}")
    minuman = "ES TEH"
elif no_makanan == 3:
    total_minuman = jml_porsi * 15000
    print(f"ES BUAH, {jml_porsi} porsi Rp.{total_minuman}")
    minuman = "ES BUAH"
elif no_makanan == 4:
    total_minuman = jml_porsi * 11000
    print(f"ES KOPI SUSU, {jml_porsi} porsi Rp.{total_minuman}")
    minuman = "ES KOPI SUSU"
elif no_makanan == 5:
    total_minuman = jml_porsi * 12000
    print(f"ICE LEMON TEA, {jml_porsi} porsi Rp.{total_minuman}")
    minuman = "ICE LEMON TEA"
else :
    print("menu minuman tidak terdaftar!")
    

    

