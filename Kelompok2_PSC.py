#Project Python Kelompok2PSC

def menu():
    print ("==================================MENU UTAMA====================================")
    print (" ")
    print ("Selamat Datang")
    print ("Sekarang Kamu ingin mengunjungi KOTA atau KABUPATEN yang ada di JAWA BARAT ?  ")
    print (" ")
    print ("1 Untuk mengunjungi KOTA")
    print ("2 Untuk mengunjungi KABUPATEN")
    print (" ") 
    print ("************************************************")
print ("======    Kamu Mau Masuk Mengunjungi Jawa Barat ?   ======")
print ("======  Isikan Data Diri Kamu Dulu Ya !!  ======")
print ("************************************************")
print (" ")
print ("Tuliskan Nama Kamu :")
nama = input()
print ("12+15")
print ("Berapa Hasil dari Penjumlahan Tersebut ?")
print ("Jawaban Kamu :")
umur = input()
if umur == ("27"):
    print (" ")
    print ("Yeay! Jawaban Kamu Benar")
    print (" ")
    print ("Selamat Datang di Jawa Barat Bos", nama)
    print (" ")
else:
    print ("Sayang sekali, jawaban kamu salah!")
    print ("Kamu dilarang masuk")
    print ("BYE !!")
    print (" ")
    print (" ")
    print (" ")
    print (" ")
    exit()


menu()

def kota():
    print (" ")
    print ("----Daftar pilihan KOTA yang dapat kamu kunjungi di JAWA BARAT----")
    print ("\n1.Bandung \n2.Bogor \n3.Bekasi \n4.Banjar \n5.Cirebon \n6.Tasikmalaya")

def kabupaten():
    print (" ")
    print ("---Daftar pilihan KABUPATEN yang dapat kamu kunjungi di JAWA BARAT---")
    print ("\n1.Karawang \n2.Kuningan \n3.Subang \n4.Purwakarta \n5.Ciamis \n6.Cianjur")

def out():
    print ("Apakah kamu sudah selesai dan ingin keluar dari program ?")
    print ("y untuk Menutup Program")
    print ("n untuk Kembali ke Menu Utama")
    print (" ")
    out = input("y/n =")
    if out == "Y":
        exit()
    elif out == "y":
        exit()
    elif out == "N":
        menu()
    elif out == "n":
        menu()
    else :
        print ("Salah input bos, Program akan segera tertutup")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        exit()
        
def keluar():
    print ("Tidak ada di pilihan bos, coba lagi dari awal? [y/n]")
    print ("y = Menu Utama")
    print ("n = Tutup Program")
    coba = input()
    if coba == "N":
        exit()
    elif coba == "n":
        exit()
    elif coba == "Y":
        menu()
    elif coba == "y":
        menu()
    else :
        print ("Salah input bos, Program akan segera tertutup")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        exit()

#Objek Wisata
Bandung = ("\n=> Kawah Putih \n=> Tangkuban Perahu \n=> Trans Studio Bandung \n=> Situ Patenggang \n=> Ciater \n=> The Lodge Maribaya \n=> Tebing Keraton")
Bogor = ("\n=> Istana Bogor \n=> Kebun Raya Bogor \n=> Jungle Land \n=> Kebun Raya Cibodas \n=> Puncak \n=> Taman Safari \n=> Taman Bunga Nusantara")
Bekasi = ("\n=> Waterboom Lippo \n=> Pantai Muara Gembong \n=> Taman Buaya Indonesia Jaya \n=> Gedung Juang 45 \n=> Danau Cibereum \n=> Go Wet Waterpark")
Banjar = ("\n=> Situ Mustika \n=> Taman Kota Lapang Bakti \n=> Dinding Hits Sumanding \n=> Taman Cinta \n=> Situ Leutik \n=> Cagar Budaya Pulo Majeti")
Cirebon = ("\n=> Keraton Kasepuhan \n=> Taman Sari Gua Sunyaragi \n=> Banyu Panas Palimanan \n=> Danau Setu Patok \n=> Outbond Siwalk")
Tasikmalaya = ("\n=> Pantai Karang Tawulan \n=> Curug Cimanintin \n=> Kebun Teh Taraju \n=> Tonjong Canyon \n=> Kampung Naga \n=> Gua Malawang")
Karawang = ("\n=> Pantai Tanjung Pakis \n=> Danau Cipule \n=> Situ Kamojing \n=> Taruma Leisure Waterpark \n=> Candi Jiwa \n=> Monumen Rawagede")
Kuningan = ("\n=> Telaga Remis \n=> Taman Wisata Alam Linggarjati \n=> Waduk Darma \n=> Cibulan \n=> Lembah Cilengkrang \n=> Gunung Ciremai")
Subang = ("\n=> Wisata Alam Capolaga \n=> Penangkaran Buaya Blanakan \n=> Desa Wisata Sri Bunihayu \n=> Bendungan Cimacan \n=> Kalijati")
Purwakarta = ("\n=> Waduk Jatiluhur \n=> Giri Tirta Kahuripan \n=> Goa Jepang dan Belanda \n=> Situ Wanayasa \n=> Desa Sajuta Batu \n=> Taman Air Mancur Sri Baduga")
Ciamis = ("\n=> Situ Lengkong Panjalu \n=> Ciung Wanara \n=> Mega Wisata Icakan \n=> Kampung Kuta \n=> Pantai Batu Hiu \n=> Curug Tujuh Cibolang")
Cianjur = ("\n=> Pantai Jayanti \n=> Curug Citambur \n=> Gunung Gede Pangrango \n=> Telaga Biru \n=> Situs Gunung Padang \n=> Kota Bunga")

while 1:

    pilih = input("Masukan Angka pilihan Kamu, kemudian tekan enter :")
    if pilih == "1":
        kota()
        print ("\n")
        print ("KOTA mana yang ingin kamu kunjungi ?")
        print ("Masukkan angka 1 sampai 6 sesuai keinginan kamu ya!")
        print (" ")
        pilih = input("KOTA Pilihanku : ")
        if pilih == "1":
            print (" ")
            print ("*****************************BANDUNG****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Bandung :")
            print (Bandung)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA BANDUNG")
            print ("\n")
            out()
        elif pilih == "2":
            print (" ")
            print ("*****************************BOGOR****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Bogor :")
            print (Bogor)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA BOGOR")
            print ("\n")
            out()
        elif pilih == "3":
            print (" ")
            print ("*****************************BEKASI****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Bekasi :")
            print (Bekasi)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA BEKASI")
            print ("\n")
            out()
        elif pilih == "4":
            print (" ")
            print ("*****************************BANJAR****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Banjar :")
            print (Banjar)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA BANJAR")
            print ("\n")
            out()
        elif pilih == "5":
            print (" ")
            print ("*****************************CIREBON****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Cirebon :")
            print (Cirebon)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA CIREBON")
            print ("\n")
            out()
        elif pilih == "6":
            print (" ")
            print ("*****************************TASIKMALAYA****************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kota Tasikmalaya :")
            print (Tasikmalaya)
            print (" ")
            print ("SELAMAT BERLIBUR DI KOTA TASIKMALAYA")
            print ("\n")
            out()
        elif pilih > "6":
            keluar()
            
    elif pilih == "2":
        kabupaten()
        print ("\n")
        print ("KABUPATEN mana yang ingin kamu kunjungi ?")
        print ("Masukkan angka 1 sampai 6 sesuai keinginan kamu ya!")
        print (" ")
        pilih = input("KABUPATEN Pilihanku : ")
        if pilih == "1":
            print (" ")
            print ("******************************KARAWANG********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Karawang :")
            print (Karawang)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN KARAWANG")
            print ("\n")
            out()
        elif pilih == "2":
            print (" ")
            print ("******************************KUNINGAN********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Kuningan :")
            print (Kuningan)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN KUNINGAN")
            print ("\n")
            out()
        elif pilih == "3":
            print (" ")
            print ("******************************SUBANG********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Subang :")
            print (Subang)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN SUBANG")
            print ("\n")
            out()
        elif pilih == "4":
            print (" ")
            print ("******************************PURWAKARTA********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Purwakarta :")
            print (Purwakarta)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN PURWAKARTA")
            print ("\n")
            out()
        elif pilih == "5":
            print (" ")
            print ("******************************CIAMIS********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Ciamis :")
            print (Ciamis)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN CIAMIS")
            print ("\n")
            out()
        elif pilih == "6":
            print (" ")
            print ("******************************CIANJUR********************************")
            print ("Berikut tempat wisata yang dapat kamu kunjungi di Kabupaten Cianjur :")
            print (Cianjur)
            print (" ")
            print ("SELAMAT BERLIBUR DI KABUPATEN CIANJUR")
            print ("\n")
            out()
        elif pilih > "6":
            keluar()

    else:
        print (" ")
        print ("Maaf bos, pilihan yang dimasukkan tidak terdaftar")
        print ("Ingin coba Lagi [y/n] ? ")
        print ("y = Kembali ke Menu Utama")
        print ("n = Tutup Program")
        coba = input()
        if coba == "Y":
            menu()
        elif coba == "y":
            menu()
        elif coba == "N":
            exit()
        elif coba == "n":
            exit()
        else:
            print ("Input Salah bos, Program akan segera tertutup")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            exit()

