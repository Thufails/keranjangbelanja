import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

total_harga = 0
keranjang = []

while True:
    clear_screen()
    print("==========","Keranjang Belanja","========")
    if keranjang == []:
        pass
    else:
        for i in range(len(keranjang)):
            print(i, "|", keranjang[i]["barang"], "=" , keranjang[i]["harga"])

    print("=====================================")
    print("Total Harga = Rp", total_harga)
    print("=====================================")
    print("=============","PILIH MENU","============")
    print("1. Tambah Barang") 
    print("2. Kembalikan Barang") 
    print("3. Hentikan Program")
    choice = int(input('\nSilakan pilih menu: '))

    if choice == 1:
        dict = {}
        print("Masukkan nama barang yang ingin anda beli")
        nama_barang = input("> ")
        dict["barang"] = nama_barang
        print("Masukkan harga barang yang anda beli")
        harga_barang = int(input("> "))
        dict["harga"] = harga_barang

        keranjang.append(dict)
        total_harga += harga_barang
    elif choice == 2:
        print("Pilih nomor barang yang ingin dihapus")
        hapus = int(input("> "))
        dict_hapus = keranjang[hapus]
        harga_barang = dict_hapus["harga"]

        total_harga -= harga_barang
        keranjang.pop(hapus)
    elif choice == 3:
        print('program berhenti')
        break