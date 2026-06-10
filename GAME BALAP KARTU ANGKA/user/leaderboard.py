from utils.file_handler import baca_file, tulis_file
from user.hash_table import HashTable

def tambah_skor(gmail_login): # Untuk menambahkan skor pemain
    data = baca_file("data/penyimpanan.txt")
    data_baru = []
    skor_baru = 1
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail_file = data[i].split(":")[1].strip()
            data_baru.append(data[i])
            data_baru.append(data[i + 1])

            if gmail_login == gmail_file:
                if i + 2 < len(data) and "Skor :" in data[i + 2]:   #Jika sudah memiliki skor, tambahkan 1
                    skor_lama = int(data[i + 2].split(":")[1])
                    skor_baru = skor_lama + 1
                    data_baru.append(f"Skor : {skor_baru}\n")
                    i += 3
                else:
                    data_baru.append("Skor : 1\n")
                    i += 2
            else:   #Untuk akun lain data disalin tanpa addanya perubahan
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    data_baru.append(data[i + 2])
                    i += 3
                else:
                    i += 2
        else:
            i += 1

    tulis_file("data/penyimpanan.txt", data_baru)   #Menyimpan data yang terbaru
    return skor_baru    #Mengembalikan skor terbaru pemain


def leaderboard(): # Untuk menampilkan leaderboard
    data = baca_file("data/penyimpanan.txt")
    if len(data) == 0:  #Jika tidak ada data
        print("\nBelum ada data!")
        return

    pemain = []
    hash_skor = HashTable()
    i = 0

    while i < len(data):    #Mengambil nama pemain dan skor dari file penyimpanan
        if "Gmail :" in data[i]:
            gmail = data[i].split(":")[1].strip()
            nama = gmail.split("@")[0]  #Nama pemain diambil sebelum tanda @
            skor = 0

            if i + 2 < len(data) and "Skor :" in data[i + 2]:   #Mengambil skor jika tersedia
                skor = int(data[i + 2].split(":")[1])
            pemain.append([nama, skor]) #Menyimpan data ke list pemain
            hash_skor.tambah_data(nama, skor)   #Menyimpan data ke hash table untuk pencarian
        i += 1

#=======================================================
#Penerapan materi Bubble Sort (alpro)
#=======================================================
    n = len(pemain) 
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if pemain[j][1] < pemain[j + 1][1]: #Membandingkan skor pemain
                pemain[j], pemain[j + 1] = pemain[j + 1], pemain[j] # Menukar posisi pemain

    print("\n===== LEADERBOARD =====")  #Menampilkan leaderboard
    ranking = 1

    for item in pemain:
        print(f"{ranking}. {item[0]} - {item[1]} kemenangan")
        ranking += 1

    while True: #Mencari skor pemain
        print("\n1. Cari skor berdasarkan nama")
        print("2. Kembali")

        pilihan = input("\nMasukkan pilihan : ")

        if pilihan == "1":
            cari_nama = input("Masukkan nama : ")
            hasil = hash_skor.cari_data(cari_nama)  #Mencari skor menggunakan hash table
            if hasil is not None:
                print(f"\n{cari_nama} : {hasil} Kemenangan")
            else:
                print(f"\nNama tidak ditemukan!")
        elif pilihan == "2":
            return
        else:
            print("Pilihan tidak tersedia!")