class Stack:             #class stack untuk menyimpan history permainan
    def __init__(self):   #inisialisasi stack kosong
        self.data = []    #list untuk menampung data stack

    def push(self, player, komputer, player_pos, komputer_pos):   #menambahkan history ke dalam stack
        histori = (                         #membuat teks history permainan
            f"Player memilih : {player}, "
            f"Posisi Player : {player_pos}, "
            f"Computer memilih : {komputer}, "
            f"Posisi Computer : {komputer_pos}"
        )

        self.data.append(histori)          #menambahkan history ke puncak stack

    def tampilkan(self):                     #menampilkan seluruh history 
        print("\n===== HISTORI STACK =====")   #menampilkan judul history
        if len(self.data) == 0:                #mengecek apakah stack kosong
            print("Belum ada histori")        #menampilkan pesan jika tidak ada history
        else:
            for item in reversed(self.data):    #menampilkan history dari yang terbaru ke yang terlama
                print(item)                     #menampilkan isi history