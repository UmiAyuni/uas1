def login():
    print('''
    ____________        _______     ____________________     __________________________
    |           \       |     |     |                  |     |                         |
    |     |\     \      |     |     |      _______     |     |    ____       _____     |
    |     | \     \     |     |     |     |       |    |     |    |   |      |    |    |
    |     |  \     \    |     |     |     |       |____|     |____|   |      |    |____|
    |     |   \     \   |     |     |     |        ____               |      |
    |     |    \     \  |     |     |     |       |    |              |      |
    |     |     \     \ |     |     |     |_______|    |         _____|      |_____
    |     |      \     \|     |     |                  |        |                  |
    |_____|       \___________|     |__________________|        |__________________|



                                - NEO CULTURE TECHNOLOGY -
    
                                         - 2021 -
 
    ''') 
    print(    "\n========================================================================================\n")
    Nama = input("Silahkan masukkan Nama Anda untuk login : ")
    
    print(    "\n========================================================================================")
    print(     "\nHallo! " + Nama + " Selamat datang Di halaman pemesanan The 3rd Album UNIVERSE NCT 2021!\n")
    print(     "Silahkan isi detail Pemesanan Anda and Happy Shopping!!!\n")
 
    Detailpilihan()
 
def akhir():
    print("\n =================================================================\n")
    print("               THANKYOU FOR ORDER & HAPPY NICE DAY !!!                ")
    print("\n =================================================================\n")

def Detailpilihan():
    print('''
    ==========================================================
                        Pre-Order The 3rd 
                     Album UNIVERSE NCT 2021
    ==========================================================
 
    Keterangan Order
    - Include direct EMS + TAX
    - Include Poster
    - Choose Version
    - Jewel Case bisa pilih member
    - Cicilan After Book Slot
    - Belum Packing Lokal
 
    ------------------------------------------------------------
    |                       KODE VERSION                       |
    |----------------------------------------------------------|
    |               PB(Photo Book)/JC(Jewel Case)              |
    |----------------------------------------------------------|
    |   Kode  |   Version  |    Payment     |       Harga      |
    |----------------------------------------------------------|
    |   PB1   | Photo Book |(Full Payment)  |  Rp. 295.000,00  |
    |   PB2   | Photo Book |( DP )          |  Rp. 150.000,00  |
    |   PB3   | Photo Book |(Book Slot)     |  Rp. 50.000,00   |
    |   JC1   | Jewel Case |(Full Payment)  |  Rp. 185.000,00  |
    |   JC2   | Jewel Case |( DP )          |  Rp. 100.000,00  |
    |   JC3   | Jewel Case |(Book Slot)     |  Rp. 50.000,00   |
    ------------------------------------------------------------
    |                  KODE METODE PEMBAYARAN                  |
    |----------------------------------------------------------|
    |       EWT(E-Wallet[Dana/Spay])/TFB(TF Bank [BCA])        |
    ------------------------------------------------------------
 
    ============================================================
    ''')
    
    PilihVersion()
 
#input
def PilihVersion():
    version = input('''Masukkan versi yang dipilih [PB/JC)] : ''')
#proses
    if version == "PB" :
        Photobook()
    elif version == "JC" :
        Jewelcase()
    else :
         print("\n ============================================================== \n")
         print("    Silahkan coba lagi, karena kode yang Anda masukkan salah ;)\n  ")
         print("    Kode Version : PB(Photo Book)/JC(Jewel Case) ")
         print("\n ============================================================== \n")
         PilihVersion()
 
def Photobook():
#input
    print("\n ============================================================== \n")
    print("----------------------------------------------------------------")
    print("| >Pemesanan 3rd Album UNIVERSE NCT 2021 [Photo Book Version]< |")
    print("----------------------------------------------------------------")
    nama1 = input("Masukkan nama Anda          : ")
    email1 = input("Masukkan E-mail Anda        : ")
    wa1 = input("Masukkan Nomor WA Anda      : ")
    alamat1 = input ("Masukkan Alamat Anda        : ")
    jumlah1 = int(input("Masukkan Jumlah album       : "))
    kode_album1 = input("Jenis Payment yang dipilih[PB1/PB2/PB3] : ")
    
#Proses
    if kode_album1 == "PB1" :
        detail1 = "Full Payment"
        version1 = "Photo Book"
        harga = 285000 
    elif kode_album1 == "PB2" :
        detail1 = "DP"
        version1 = "Photo Book"
        harga = 150000
    elif kode_album1 == "PB3" :
        detail1 = "Book Slot"
        version1 = "Photo Book" 
        harga = 50000
    else :
        print("\n----------------------------------------------------------------\n")
        list = str(input('''Kode Payment yang Anda masukkan salah, 
        Apakah Anda ingin melihat list kode payment ? [Y] : '''))
        if list == "Y" or list == "y":
         listKode = [
          "\n^LIST KODE PAYMENT PHOTO BOOK VERSION^", "PB1;Photobook(Fullpayment)", "PB2;PhotoBook(DP)", "PB3;PhotoBook(BookSlot)"
          ]
        for Kode in listKode:
            print(Kode)
        else:
            Photobook()
 
    metode = input("Masukkan metode pembayaran [EWT/TFB]    : ")
    if metode == "EWT" :
        D_metode = "E-Wallet [Dana&Spay] 083816716161 a/n Buna" 
    elif metode == "TFB" :
        D_metode = "Transfer Bank [BCA] 3300023060 a/n Buna"
    else :
        print("\n =================================================================== \n")
        print("Kode Metode Pembayaran yang Anda masukkan salah,silahkan coba lagi :)\n")
        print("Kode Metode Pembayaran : EWT(E-Wallet[Dana/Spay])/TFB(TF Bank [BCA])")
        Photobook()
#Output
    if kode_album1 == 'PB1' or kode_album1 == 'PB2' or kode_album1 == 'PB3':
        print("\n ==================================================================")
        print("| >.<Pemesanan 3rd Album UNIVERSE NCT 2021 [Photo Book Version]>.< |")
        print(" ==================================================================")
        print(" Nama Pemesan        : " +str(nama1))
        print(" E-mail Pemesan      : " +str(email1))
        print(" Nomor WA            : " +str(wa1))
        print(" Alamat              : "  +str(alamat1))
        print(" Jenis Payment       : " +str(detail1))
        print(" Album Version       : " +str(version1))
        print(" Jumlah Album        : " ,(jumlah1), "pcs")
        total1=int(jumlah1*harga)
        print(" Jumlah yang dibayar :  Rp." ,(total1))
        print(" Metode Pembayaran   : " ,(D_metode))
        print("\n =================================================================\n")
        print("                   TERIMAKASIH ATAS PESANANNYA !!!                    ")            
        print("\n =================================================================\n")
        ulang=str(input("Apakah Anda ingin memesan lagi? [Y/N] : "))
        while ulang == "Y":
            Detailpilihan()
        else :
            akhir()
 
def Jewelcase():
#input
    print("\n ==================================================================\n")
    print("----------------------------------------------------------------")
    print("| >Pemesanan 3rd Album UNIVERSE NCT 2021 [Jewel Case Version]< |")
    print("----------------------------------------------------------------")
    nama2 = input("Masukkan nama Anda           : ")
    email2 = input("Masukkan E-mail Anda         : ")
    wa2 = input("Masukkan Nomor WA Anda       : ")
    alamat2 = input ("Masukkan Alamat Anda         : ")
    jumlah2 = int(input("Masukkan Jumlah album        : "))
    nama_m = input("Masukkan Nama member yang dipilih        : ")
    kode_album2 = input("Jenis Payment yang dipilih[JC1/JC2/JC3]  : ")
#proses
    if kode_album2 == "JC1" :
        detail2 = "Full Payment"
        version2 = "Jewel Case"
        harga = 185000
    elif kode_album2 == "JC2" :
        detail2 = "DP"
        version2 = "Jewel Case"
        harga = 100000
    elif kode_album2 == "JC3" :
        detail2 = "Book Slot"
        version2 = "Jewel Case"
        harga = 50000
 
    else :
        print("\n----------------------------------------------------------------\n")
        list2 = str(input('''Kode Payment yang Anda masukkan salah, 
        Apakah Anda ingin melihat list kode payment ? [Y] : '''))
        if list2 == "Y" or list2 == "y":
         listKode2 = [
          "\n^LIST KODE PAYMENT JEWELCASE VERSION^", "JC1;Jewel Case(Fullpayment)", "JC2;Jewel Case(DP)", "JC3;Jewel Case(BookSlot)"
          ]
        for Kode in listKode2:
            print(Kode)
        else:
            Jewelcase() 
 
    metode = input("Masukkan metode pembayaran [EWT/TFB]     : ")
    if metode == "EWT" :
        D_metode = "E-Wallet [Dana&Spay] 083816716161 a/n Buna" 
    elif metode == "TFB" :
        D_metode = "Transfer Bank [BCA] 3300023060 a/n Buna"
    else :
        print("\n====================================================================\n")
        print("Kode Metode Pembayaran yang Anda masukkan salah,silahkan coba lagi :)\n")
        print("Kode Metode Pembayaran : EWT(E-Wallet[Dana/Spay])/TFB(TF Bank [BCA])")
        Jewelcase()
 
#output
    if kode_album2 == 'JC1' or kode_album2 == 'JC2' or kode_album2 == 'JC3' :
        print("\n ==================================================================")
        print("| >.<Pemesanan 3rd Album UNIVERSE NCT 2021 [Jewel Case Version]>.< |")
        print(" ==================================================================")
        print(" Nama Pemesan        : " +str(nama2))
        print(" E-mail Pemesan      : " +str(email2))
        print(" Nomor WA            : " +str(wa2))
        print(" Alamat              : "  +str(alamat2))
        print(" Jenis Payment       : " +str(detail2))
        print(" Album Version       : " +str(version2))
        print(" Member yang Dipilih : " +str(nama_m))
        print(" Jumlah Album        : " ,(jumlah2), "pcs")
        total2=int(jumlah2*harga)
        print(" Jumlah yang dibayar :  Rp." ,(total2)) 
        print(" Metode Pembayaran   : " ,(D_metode))
        print("\n =================================================================\n")
        print("                   TERIMAKASIH ATAS PESANANNYA !!!                    ")            
        print("\n =================================================================\n")
        ulang=str(input("Apakah Anda ingin memesan lagi? [Y/N] : "))
        while ulang == "Y":
            Detailpilihan()
        else :
            akhir()


login()
