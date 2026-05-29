import random

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan data angka baru
        self.next = None # Pointer ke node berikutnya

class CircularLinkedList:
    def __init__(self):
        self.head = None # Node pertama
        self.current = None # Node yang sedang digunakan
        self.jumlah = 0 # Jumlah total node
        self.terpakai = 0 # Jumlah kartu yang sudah terpakai

    def buat_kartu(self, data):
        prev = None
        for angka in data: # Perulangan untuk memasukkan setiap angka ke node
            node_baru = Node(angka)
            if self.head is None: # Jika head masih kosong
                self.head = node_baru
            else:
                prev.next = node_baru # Menghubungkan node sebelumnya ke node baru
            prev = node_baru
            self.jumlah += 1

        # node terakhir menunjuk ke head
        prev.next = self.head
        self.current = self.head # current dimulai dari head

    def ambil(self, angka): # untuk mengambil kartu berdasarkan angka
        if self.current is None:
            return False
        temp = self.current

        for _ in range(self.jumlah):
            if temp.data == angka: # jika angka ditemukan
                temp.data = None
                self.terpakai += 1
                return True
            temp = temp.next # pindah ke node berikutnya
        return False # Jika angka tidak ditemukan

    def tersedia(self, angka): # Untuk ngecek apakah kartu masih tersedia
        temp = self.head
        for _ in range(self.jumlah):
            if temp.data == angka:
                return True
            temp = temp.next
        return False

    def tampilkan(self): # Untuk menampilkan semua kartu yang belum dipakai
        hasil = []
        temp = self.head
        for _ in range(self.jumlah):
            if temp.data is not None:
                hasil.append(temp.data)
            temp = temp.next
        return hasil

    def reset(self): # Untuk mengembalikan kartu ke kondisi awal
        data_awal = [1, 2, 3, 4, 5, 6]
        temp = self.head
        for angka in data_awal: # Mengisi ulang data pada setiap node
            temp.data = angka
            temp = temp.next
        self.terpakai = 0 # Mengatur ulang jumlah kartu terpakai