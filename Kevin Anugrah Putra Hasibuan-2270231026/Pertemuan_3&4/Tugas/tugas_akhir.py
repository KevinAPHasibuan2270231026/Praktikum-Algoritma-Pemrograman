#Buatlah sebuah aplikasi Kasir bertema bebas, TETAPI tidak boleh memiliki tema yang sama 
#dengan satu sama lainnya.
#• Nama pelanggan
#• Alamat
#• No Telp
#• Tanggal
#• Harga per barang
#• Harga total
#Laporan Praktikum. 
print('''
==================================   
        Penjualan Cat Tembok
=================================
        Pilihan Cat
-------------------------------------
|kode|Nama        |      Harga       |
|AC  |Cat Dasar   |Rp. 20.000,00        |
|AD  |Cat Remover |Rp. 25.000,00       |
|AB  |Cat Top Coat|Rp. 35.000,00        |


''')
input("masukan nama anda :")
input("masukan alamat anda :")
input("masukan nomor telepon anda :")
print("Kasir Pembelian Cat Tembok")
print("Anda Mau Pesan Apa?\n\nJika Cat Tekan 1\n\n")
opsi = int(input("1/2 :"))
if opsi == 1 :
    kode = input("Masukan Kode :")
    n= int(input("tanggal Pesanan : "))
    n = int(input("Jumlah Pesanan :"))
    if kode == "AC" :
        print(f'\nKode = {kode}\nNama Cat = Cat Dasar\nHarga = Rp.20.000\nTotal Bayar = Rp.{n*20000},00\n')
        print("------Terima Kasih-------")
        print()
    elif kode == "AD" :
        print(f'\nKode = {kode}\nNama Cat = Cat Dasar\nHarga = Rp.25.000\nTotal Bayar = Rp.{n*25000},00\n')
        print("------Terima Kasih-------")
    elif kode == "AB" :
        print(f'\nKode = {kode}\nNama Cat = Cat Dasar\nHarga = Rp.35.000\nTotal Bayar = Rp.{n*35000},00\n')
        print("------Terima Kasih-------")
    else :
        print(" Menu Tidak Tersedia")
        
        
        
        