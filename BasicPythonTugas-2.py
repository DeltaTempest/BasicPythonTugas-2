daftarKontak = {
    
}

def seeContactList(daftarKontak):
    print("\nDaftar kontak:\n")
    for names in daftarKontak:
        print("Nama: ", names, "\nNo Telepon: ", daftarKontak[names], "\n")
    

def addContacts(names, noTelp):
    daftarKontak[names] = noTelp
    print("\nContact succseccfully added!\n")


print("Selamat Datang!\n")


while True:
    print("---Menu---\n1. Daftar Kontak\n2. Tambah Kontak\n3. Keluar\n")
    numbers = int(input("Silahkan masukan nomor: \n"))
    
    if numbers == 1:
        if len(daftarKontak) == 0:
            print("Contact is empty! Please add contact first!\n")
        else:
            seeContactList(daftarKontak)
        
        
    elif numbers == 2:
        nama = input("Nama: ")
        nomor = input("No Telp: ")
        addContacts(nama, nomor)
    elif numbers ==  3:
        print("Program is done, Goodbye!")
        break;
    else:
        print("Please input the rigth numbers!\n")

