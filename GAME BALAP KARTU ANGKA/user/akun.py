from utils.file_handler import baca_file

def gmail_sudah_ada(gmail): #Mengecek apakah email sudah ada di file penyimpanan
    data = baca_file("data/penyimpanan.txt")    #Membaca data dari file penyimpanan
    for line in data:
        if gmail in line:
            return True
    return False

def cek_login(gmail, password):     #Verifikasi gmail dan pw saat login
    data = baca_file("data/penyimpanan.txt")
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail_file = data[i].split(":")[1].strip()
            if i + 1 < len(data):
                password_file = data[i + 1].split(":")[1].strip()
                if gmail == gmail_file and password == password_file:   #membandingkan gmail dan pw yg di input dengan yg ada di .txt
                    return True
        i += 1
    return False    #kalau data tidak ditemukan