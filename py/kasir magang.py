def menu_utama():
    while True:
        print("Menu Utama")
        print("1. Pilihan 1")
        print("2. Pilihan 2")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            pilihan_1()
        elif pilihan == '2':
            pilihan_2()
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def pilihan_1():
    while True:
        print("Anda memilih pilihan 1.")
        print("| ====================== |")
        print("| 1. ES JERUK      RP.10000 |")
        print("| 2. ES TEH        RP.5000  |")
        print("| 3. JUS BUAH      RP.15000 |")
        print("| 4. ES KOPI SUSU  RP.11000 |")
        print("| 5. ICE LEMON TEA RP.12000 |")
        print("| 6. Kembali ke menu utama  |")
        print("| ====================== |")
   
        no_minuman = int(input("Masukkan nomor minuman: "))
        
        if no_minuman == 6:
            return  # Kembali ke menu utama
        
        jml_porsi = int(input("Masukkan jumlah pesanan kamu: "))
        
        if no_minuman == 1:
            total_minuman = jml_porsi * 10000
            print(f"ES JERUK, {jml_porsi} porsi Rp.{total_minuman}")
        elif no_minuman == 2:
            total_minuman = jml_porsi * 5000
            print(f"ES TEH, {jml_porsi} porsi Rp.{total_minuman}")
        elif no_minuman == 3:
            total_minuman = jml_porsi * 15000
            print(f"JUS BUAH, {jml_porsi} porsi Rp.{total_minuman}")
        elif no_minuman == 4:
            total_minuman = jml_porsi * 11000
            print(f"ES KOPI SUSU, {jml_porsi} porsi Rp.{total_minuman}")
        elif no_minuman == 5:
            total_minuman = jml_porsi * 12000
            print(f"ICE LEMON TEA, {jml_porsi} porsi Rp.{total_minuman}")
        else:
            print("Nomor minuman tidak valid.")
        
        kembali = input("Kembali ke menu utama? (y/n): ")
        if kembali.lower() == 'y':
            return

def pilihan_2():
    print("Anda memilih pilihan 2.")
    kembali = input("Kembali ke menu utama? (y/n): ")
    if kembali.lower() == 'y':
        return
    else:
        print("Pilihan tidak valid, kembali ke menu utama.")
        return

# Memanggil fungsi menu utama untuk memulai program
menu_utama()
