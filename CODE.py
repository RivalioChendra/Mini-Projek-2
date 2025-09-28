from prettytable import PrettyTable
import pwinput

# Data hutang
daftar_hutang = {
    1: ("Dapa", "50000"),
    2: ("Darma", "75000"),
    3: ("Zyrus", "100000")
}

# Data login (username, password, role)
users = {
    "admin": ("123", "Manager"),
    "budak": ("111", "Karyawan"),
    "user": ("222", "Viewer")
}

# Fungsi tampiin data
def lihat_data():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Jumlah Hutang"]
    for id in daftar_hutang:
        nama, jumlah = daftar_hutang[id]
        tabel.add_row([id, nama, jumlah])
    print(tabel)

# Fungsi tambah data 
def tambah_data():
    try:
        nama = input("Masukkan nama: ")
        jumlah = input("Masukkan jumlah hutang: ")
        if not jumlah.isdigit():  
            raise ValueError("Jumlah harus angka bulat saja")
        id_baru = len(daftar_hutang) + 1   
        daftar_hutang[id_baru] = (nama, jumlah)
        print("Data berhasil ditambahkan!")
    except ValueError as e:
        print(e)

# Fungsi ubah data
def ubah_data():
    lihat_data()
    try:
        id_edit = int(input("Masukkan ID yang mau diubah: "))
        if id_edit in daftar_hutang:
            nama = input("Nama baru: ")
            jumlah = input("Jumlah hutang baru: ")
            if not jumlah.isdigit():
                raise ValueError("Jumlah hutang harus angka bulat saja")
            daftar_hutang[id_edit] = (nama, jumlah)
            print("Data berhasil diubah!")
        else:
            print("ID tidak ditemukan!")
    except ValueError as e:
        print(e)

# Fungsi hapus data
def hapus_data():
    lihat_data()
    try:
        id_hapus = int(input("Masukkan ID yang mau dihapus: "))
        if id_hapus in daftar_hutang:
            terhapus = daftar_hutang.pop(id_hapus)
            print("Data", terhapus[0], "berhasil dihapus")
        else:
            print("ID tidak ditemukan")
    except ValueError:
        print("ID harus berupa angka")

# Menu utama sesuai role
def menu(role):
    while True:
        print("\n=== MENU", role, "===")  
        if role == "Manager":
            print("1. Tambah Hutang")
            print("2. Lihat Hutang")
            print("3. Ubah Hutang")
            print("4. Hapus Hutang")
            print("5. Keluar Program")
        elif role == "Karyawan":
            print("1. Tambah Hutang")
            print("2. Lihat Hutang")
            print("3. Ubah Hutang")
            print("4. Keluar Program")
        elif role == "Viewer":
            print("1. Lihat Hutang")
            print("2. Keluar Program")

        pilihan = input("Pilih menu: ")

        if role == "Manager":
            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                lihat_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                hapus_data()
            elif pilihan == "5":
                print("Keluar program...")
                break
            else:
                print("Menu tidak tersedia!5")

        elif role == "Karyawan":
            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                lihat_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                print("Keluar program...")
                break
            else:
                print("Menu tidak tersedia!")

        elif role == "Viewer":
            if pilihan == "1":
                lihat_data()
            elif pilihan == "2":
                print("Keluar program...")
                break
            else:
                print("Menu tidak tersedia!")

# sistem login
def login():
    while True:
        print("\n=== LOGIN ===")
        user = input("Username: ")
        password = pwinput.pwinput("Password: ")
        if user in users and users[user][0] == password:
            role = users[user][1]
            print("Login berhasil sebagai", role)
            menu(role)
            break
        else:
            print("Username atau password salah, coba lagi!")


login()
