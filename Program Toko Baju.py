print("Selamat Datang")
# Input Awalan
nama_pembeli = input("Masukkan Nama Lengkap anda : ")
no_hp = input("Masukkan No. Handphone anda : ")
gender = input("Jenis Kelamin [Pria/Wanita] : ")
belibarang = int(input("Banyaknya Pembelian Barang (max.10) : "))

# List
list_nama_barang = []
list_harga = []
list_ukuran = []
list_jumlah_beli = []
list_subtotal = []


# Fungsi Def
def bajuPria():
    print("Product baju pria")
    print("1. Jas")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp1.500.000,00,-")
    print()
    print("2. Kemeja")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp100.000,00,-")
    print()
    print("3. Kemeja Denim")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp150.000,00,-")
    print()
    print("4. Batik")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp150.000,00,-")
    print()
    print("5. Baju Koko")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp100.000,00,-")
    print()
    print("6. Kaos Polos")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp50.000,00,-")
    print()
    print("7. Rompi")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp150.000,00,-")
    print()
    print("8. Jaket Parka")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp200.000,00,-")
    print()
    print("9. Jaket Kulit")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp400.000,00,-")
    print()
    print("10. Jaket Windproof")
    print("    Ukuran [S/M/L/XL]")
    print("    Harga : Rp850.000,00,-")
    print()
    return


def bajuWanita():
    print("Product baju wanita")
    print("1. Dress Pesta")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp500.000,00,-")
    print()
    print("2. Kemeja")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp150.000,00,-")
    print()
    print("3. Gamis")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp110.000,00,-")
    print()
    print("4. Daster")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp85.000,00,-")
    print()
    print("5. T-Shirt")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp75.000,00,-")
    print()
    print("6. Cardigan")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp50.000,00,-")
    print()
    print("7. Blazer")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp100.000,00,-")
    print()
    print("8. Blouse")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp120.000,00,-")
    print()
    print("9. Jumpsuit")
    print("   Ukuran [S/M/L/XL]")
    print("   Harga : Rp170.000,00,-")
    print()
    print("10. Piyama")
    print("    Ukuran [S/M/L/XL]")
    print("    Harga : Rp135.000,00,-")
    print()
    return


print()
# Percabangan & Perulangan
for i in range(belibarang):
    print("Pembelian barang ke- " + str(i + 1))
    if gender == "PRIA" or gender == "Pria" or gender == "pria" or gender == "MALE" or gender == "Male" or gender == "male" or gender == "COWO" or gender == "Cowo" or gender == "cowo" or gender == "laki laki":
        bajuPria()
        pilihan_baju = input("Masukkan Pilihan Baju [1 ~ 10] : ")
        ukuran_baju = input("Ukuran [S/M/L/XL] : ")
        if ukuran_baju == "S" or ukuran_baju == "s":
            ukuran = "S"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "M" or ukuran_baju == "m":
            ukuran = "M"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "L" or ukuran_baju == "l":
            ukuran = "L"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
            ukuran = "XL"
            list_ukuran.append(ukuran)
        else:
            print()
            print("     Tidak diketahui ukurannya")
            print()
        jumlah_beli = int(input("Mau beli berapa? : "))
        list_jumlah_beli.append(jumlah_beli)
        if pilihan_baju == "1" or pilihan_baju == "Jas":
            nama_barang = "Jas"
            list_nama_barang.append(nama_barang)
            harga = 1500000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "2" or pilihan_baju == "Kemeja":
            nama_barang = "Kemeja"
            list_nama_barang.append(nama_barang)
            harga = 100000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "3" or pilihan_baju == "Kemeja Denim":
            nama_barang = "Kemeja Denim"
            list_nama_barang.append(nama_barang)
            harga = 150000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "4" or pilihan_baju == "Batik":
            nama_barang = "Batik"
            list_nama_barang.append(nama_barang)
            harga = 150000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "5" or pilihan_baju == "Baju Koko":
            nama_barang = "Baju Koko"
            list_nama_barang.append(nama_barang)
            harga = 100000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "6" or pilihan_baju == "Kaos Polos":
            nama_barang = "Kaos Polos"
            list_nama_barang.append(nama_barang)
            harga = 50000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "7" or pilihan_baju == "Rompi":
            nama_barang = "Rompi"
            list_nama_barang.append(nama_barang)
            harga = 150000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "8" or pilihan_baju == "Jaket Parka":
            nama_barang = "Jaket Parka"
            list_nama_barang.append(nama_barang)
            harga = 200000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "9" or pilihan_baju == "Jaket Kulit":
            nama_barang = "Jaket Kulit"
            list_nama_barang.append(nama_barang)
            harga = 400000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "10" or pilihan_baju == "Jaket Windproof":
            nama_barang = "Jaket Windproof"
            list_nama_barang.append(nama_barang)
            harga = 850000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        else:
            print("Kode baju salah")
            print("Baju tidak ditemukan")
            continue
        print()
        selesai = input("Apakah mau belanja lgi [Ya/Tidak] : ")
        if selesai == "Tidak" or selesai == "tidak" or selesai == "No" or selesai == "no" or selesai == "Ga" or selesai == "ga" or selesai == "Gk" or selesai == "gk" or selesai == "gk ah" or selesai == "Ngga" or selesai == "ngga" or selesai == "ngga mau" or selesai == "cukup":
            break
        print()
    elif gender == "WANITA" or gender == "Wanita" or gender == "wanita" or gender == "FEMALE" or gender == "Female" or gender == "female" or gender == "CEWE" or gender == "Cewe" or gender == "cewe" or gender == "Perempuan":
        bajuWanita()
        pilihan_baju = input("Masukkan Pilihan Baju [1 ~ 10] : ")
        ukuran_baju = input("Ukuran [S/M/L/XL] : ")
        if ukuran_baju == "S" or ukuran_baju == "s":
            ukuran = "S"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "M" or ukuran_baju == "m":
            ukuran = "M"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "L" or ukuran_baju == "l":
            ukuran = "L"
            list_ukuran.append(ukuran)
        elif ukuran_baju == "XL" or ukuran_baju == "Xl" or ukuran_baju == "xl":
            ukuran = "XL"
            list_ukuran.append(ukuran)
        else:
            print()
            print("     Tidak diketahui ukurannya")
            print()
        jumlah_beli = int(input("Mau beli berapa? : "))
        list_jumlah_beli.append(jumlah_beli)
        if pilihan_baju == "1" or pilihan_baju == "Dress Pesta":
            nama_barang = "Dress Pesta"
            list_nama_barang.append(nama_barang)
            harga = 500000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "2" or pilihan_baju == "Kemeja":
            nama_barang = "Kemeja"
            list_nama_barang.append(nama_barang)
            harga = 150000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "3" or pilihan_baju == "Gamis":
            nama_barang = "Gamis"
            list_nama_barang.append(nama_barang)
            harga = 110000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "4" or pilihan_baju == "Daster":
            nama_barang = "Daster"
            list_nama_barang.append(nama_barang)
            harga = 85000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "5" or pilihan_baju == "T-Shirt":
            nama_barang = "T-Shirt"
            list_nama_barang.append(nama_barang)
            harga = 75000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "6" or pilihan_baju == "Cardigan":
            nama_barang = "Cardigan"
            list_nama_barang.append(nama_barang)
            harga = 50000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "7" or pilihan_baju == "Blazer":
            nama_barang = "Blazer"
            list_nama_barang.append(nama_barang)
            harga = 100000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "8" or pilihan_baju == "Blouse":
            nama_barang = "Blouse"
            list_nama_barang.append(nama_barang)
            harga = 120000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "9" or pilihan_baju == "Jumpsuit":
            nama_barang = "Jumpsuit"
            list_nama_barang.append(nama_barang)
            harga = 170000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        elif pilihan_baju == "10" or pilihan_baju == "Piyama":
            nama_barang = "Piyama"
            list_nama_barang.append(nama_barang)
            harga = 135000
            list_harga.append(harga)
            sub_total = list_harga[i] * list_jumlah_beli[i]
            list_subtotal.append(sub_total)
        else:
            print("Kode baju salah")
            print("Baju tidak ditemukan")
            continue
        print()
        selesai = input("Apakah mau belanja lgi [Ya/Tidak] : ")
        if selesai == "Tidak" or selesai == "tidak" or selesai == "No" or selesai == "no" or selesai == "Ga" or selesai == "ga" or selesai == "Gk" or selesai == "gk" or selesai == "gk ah" or selesai == "Ngga" or selesai == "ngga" or selesai == "ngga mau" or selesai == "cukup":
            break
        print()
    else:
        print()
        print("                 Jenis Kelamin Salah")
        break

# Output Program
print()
print("=" * 70)
print("                          Program Toko Baju")
print("                             Kelompok 8")
print("=" * 70)
print()
print("                            " + str(nama_pembeli))
print("                             " + str(no_hp))
print()
print("Daftar Belanjaan :")
print("=" * 100)
print("Nama barang \t\t\t\t\t Ukuran \t\t\t Jumlah \t\t Harga \t\t\t Subtotal")
print("=" * 100)
for i in range(belibarang):
    print("%s\t\t\t\t\t\t\t%s\t\t\t\t\t%i\t\t\t\t%i\t\t\t%i" % (list_nama_barang[i], list_ukuran[i], list_jumlah_beli[i], list_harga[i], list_subtotal[i]))
print("-" * 100)

# Total Jumlah Harga Seluruh Barang Belanjaan
Total = sum(list_subtotal)

print("Total belanja : Rp" + str(Total))

# Pemberian Diskon
if Total >= 500000:
    print()
    print("Selamat!")
    print("Anda Mendapatkan Diskon 25%")
    diskon = Total * 25 / 100
else:
    diskon = 0
print()

jumlah_bayar = Total - diskon

print("Total Akhir : Rp" + str(jumlah_bayar))
print("-" * 70)

# Pembayaran
Ubyr = int(input("Bayar : Rp"))

# Uang Kembalian
uangkembalian = Ubyr - jumlah_bayar
if uangkembalian == 0:
    print()
else:
    print()
    print("Uang Kembalian : Rp", str(uangkembalian))

print()
print("                     Terima Kasih sudah belanja :)")

