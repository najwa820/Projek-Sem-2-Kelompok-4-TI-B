from utils.file_handler import tambah_file
from user.akun import gmail_sudah_ada

def register():
    gmail = input("Masukkan Gmail : ") #Input gmail
    if gmail_sudah_ada(gmail):  # Cek udh terdaftar atau blm
        print("\nGmail sudah terdaftar!")
        return  # kalau udh langsung return / bergenti prodes registrasinya

    password = input("Masukkan Password : ")    # buat pw

    if len(password) < 6:
        print("Password minimal 6 karakter!")
        return

    data = (    #susunn data pengguna sperti di bawah
        f"Gmail : {gmail}\n"
        f"Password : {password}\n"
    )

    tambah_file("data/penyimpanan.txt", data)   # simpan data ke file
    print("\nREGISTER berhasil!")