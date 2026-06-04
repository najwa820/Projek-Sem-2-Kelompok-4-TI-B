from user.akun import cek_login

def login():
    gmail = input("Masukkan Gmail : ")  # input gmail
    password = input("Masukkan Password : ")    #input pw
    berhasil = cek_login(gmail, password)   #nge cek cocok ga email dgn pw nya

    if berhasil:
        nama = gmail.split("@")[0]
        print(f"\nSelamat Datang {nama}!")
        return gmail
    print("\nGmail atau Password salah!")
    return None