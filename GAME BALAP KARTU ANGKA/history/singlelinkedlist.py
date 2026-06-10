#=======================================================
#Penerapan materi Single Linked List (matkul strukdat)
#=======================================================

class Node:                   #class node untuk menyimpan satu data history 
    def __init__(self, isiHistory):     #inisialisasi node baru
        self.isiHistory = isiHistory     #menyimpan isi histroy permainan
        self.sambung = None              #menyimpan alamat node berikutnya

class SingleLinkedList:             #class single linked list
    def __init__(self):             #inisialisasi linked list kosong
        self.awal = None            #membuat node baru
    
    def tambah_history(self, hasilGame):      #menambah history  baru ke linked list
        rondeBaru = Node(hasilGame)           #membuat node baru
        if self.awal is None:                 #mengecek apakah linked list kosong
            self.awal = rondeBaru             #node baru menjadi node pertama
        else:
            bantu = self.awal                  #variabel baru mulai dari node pertama
            while bantu.sambung is not None:  #mencari node terakhir
                bantu = bantu.sambung         #pindah ke node berikutnya
            bantu.sambung = rondeBaru         #menyambungkan  node trakhir dengan node baru

    def tampilkan_history(self):             #menampilkan seluruh history permainan
        bantu = self.awal                    #variabel bantuk untuk menelusuri linkedlist
        nomor = 1                            #nomor urut histroy
        if self.awal is None:                #mengecek apakah linked list kosong
            print("History kosong")          #menampilkan pesan jika tidak ada history
        else:
            while bantu is not None:         #menampilkan seluruh data history
                print(f"{nomor}. {bantu.isiHistory}")   #menampilkan nomor dan isi history
                bantu = bantu.sambung         #pindah ke node berikutnya
                nomor += 1                     #menambah nomor urut