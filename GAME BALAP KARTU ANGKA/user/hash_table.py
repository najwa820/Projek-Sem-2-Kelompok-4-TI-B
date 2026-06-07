class HashTable:    #Untuk menyimpan dan mengelola data skor pemain
    def __init__(self):
        self.data = {}

    def tambah_data(self, nama, skor):  #Menambahkan data nama dan skor
        self.data[nama] = skor

    def cari_data(self, nama):  #Mencari skor berdasarkan nama pemain
        if nama in self.data:   #Jika nama ditemukan, kembalikan skor
            return self.data[nama]
        else:
            return None #Jika nama tidak ditemukan, kembalikan None

    def tampilkan(self):    #Menampilkan seluruh data nama dan skor
        for nama in self.data:
            print(f"{nama} : {self.data[nama]}")