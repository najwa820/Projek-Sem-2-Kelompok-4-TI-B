from utils.file_handler import tambah_file
from user.akun import gmail_sudah_ada

def register():
    gmail = input("Masukkan Gmail : ") #Input gmail
    if gmail_sudah_ada(gmail):  #Mengecek apakah sudah terdaftar atau belum
        print("\nGmail sudah terdaftar!")
        return  #Jika sudah langsung return / berhenti proses registrasinya

    password = input("Masukkan Password : ")    #Membuat pw

    if len(password) < 6:
        print("Password minimal 6 karakter!")
        return

    data = (    #susun data pengguna sperti di bawah
        f"Gmail : {gmail}\n"
        f"Password : {password}\n"
    )

    tambah_file("data/penyimpanan.txt", data)   #Simpan data ke file penyimpanan
    print("\nREGISTER berhasil!")