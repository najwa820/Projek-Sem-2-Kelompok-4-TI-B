class Node:
    def __init__(self, history):     #untuk membuat node baru
        self.history = history        # Menyimpan isi history
        self.next = None               # Menyimpan alamat node berikutnya

        self.prev = None                # Menyimpan alamat node sebelumnya

class DoubleLinkedList:               # Class Double Linked List untuk mengelola data history
    def __init__(self):
        self.head = None                    # Menunjuk node pertama
        self.current = None                    # Menunjuk node yang sedang aktif
    
    # Tambah History
    def tambah_history(self, hasil):
        node_baru = Node(hasil)                # Membuat node baru

        # JIKA KOSONG
        if self.head is None:               # Mengecek apakah linked list kosong
            self.head = node_baru             # Node baru menjadi head
            self.current = node_baru           # Current menunjuk ke node baru

        else:
            bantu = self.head        # variabel bantu mulai dari  head                   
            while bantu.next is not None:  # Mencari node terakhir
                bantu = bantu.next   #pindah ke node berikutny      
            bantu.next = node_baru    # menghubungkan node terakhir ke node baru
            node_baru.prev = bantu     # menghubungkan node baru ke node sebelumnya

    # Tampilkan History Sekarang
    def tampilkan_current(self):
        if self.current is not None:      #mengecek apakah current ada
            print(f"\nHistory sekarang : {self.current.history}")        #menampilkan isi history
        else:
            print("History kosong")       #menampilkan pesan jika history kosong

    # Next History
    def next_history(self):     #metode untuk berpindah history berikutnya
        if self.current is not None and self.current.next is not None:     #mengecek apakah current dan next tersedia 
            self.current = self.current.next        #pindah ke node berikutnya
            self.tampilkan_current()               #menmapilkan history yang baru
        else:
            print("Tidak ada history berikutnya")       #menampilkan pesan jika tidak ada history  berikutnya

    # Previous History
    def prev_history(self):      #metode untuk berpindah  ke history sebelumnya
        if self.current is not None and self.current.prev is not None:   #mengecek apakah current dan prev tersedia
            self.current = self.current.prev    #pindah ke node sebelumnya
            self.tampilkan_current()           #menampilkan history yang baru
        else:
            print("Tidak ada history sebelumnya")     #menampilkan pesan jika tidak ada history sebelumnya