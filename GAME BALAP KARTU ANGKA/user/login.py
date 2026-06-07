from user.akun import cek_login

def login():    #Fungsi untuk proses login player
    gmail = input("Masukkan Gmail : ")  #Input gmail
    password = input("Masukkan Password : ")    #Input pw
    berhasil = cek_login(gmail, password)   #nMengecek cocok atau tidak email dgn pw nya

    if berhasil:    #Jika berhasil
        nama = gmail.split("@")[0]  #Mengambil nama sebelum tanda @
        print(f"\nSelamat Datang {nama}!")
        return gmail
    print("\nGmail atau Password salah!")
    return None