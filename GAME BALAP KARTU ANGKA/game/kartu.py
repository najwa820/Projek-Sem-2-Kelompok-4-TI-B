from game.circularlinkedlist import CircularLinkedList

class Kartu:    #Kelas untuk mengelola kumpulan kartu pemain
    def __init__(self):
        self.kartu = CircularLinkedList()
        self.kartu.buat_kartu([1,2,3,4,5,6])    #Mengisi kartu dengan angka 1-6

    def tampilkan(self):    #Menampilkan kartu apa saja yang masih tersedia
        return self.kartu.tampilkan()

    def tersedia(self, angka):  #Mengecek apakah kartu dengan angka tertentu masih tersedia
        return self.kartu.tersedia(angka)

    def gunakan(self, angka):   #Menghapus kartu yang telah digunakan dari daftar kartu
        self.kartu.ambil(angka)

    def reset(self):    #Mengembalikan kartu ke kondisi awal 1-6
        self.kartu.reset()