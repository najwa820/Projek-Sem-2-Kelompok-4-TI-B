from user.login import login # MENGAMBIL FUNGSI login DARI DALAM FOLDER user DI FILE login.py
from user.register import register # MENGAMBIL FUNGSI register DARI DALAM FOLDER user DI FILE register.py
from user.leaderboard import leaderboard # MENGAMBIL FUNGSI leaderboard DARI DALAM FOLDER user DI FILE leaderboard.py
from history.singlelinkedlist import SingleLinkedList # MENGAMBIL CETAKAN class SingleLinkedList DARI FOLDER history
from history.doublelinkedlist import DoubleLinkedList # MENGAMBIL CETAKAN class DoubleLinkedList DARI FOLDER history

history_game = SingleLinkedList() # MEMBUAT OBJEK TEMPAT BARU BERNAMA history_game MENGGUNAKAN STRUKTUR Single Linked List
history_double = DoubleLinkedList() # MEMBUAT OBJEK TEMPAT BARU BERNAMA history_double MENGGUNAKAN STRUKTUR DoubleLinkedList

from game.game import mulai_game # MENGAMBIL FUNGSI mulai_game DARI DALAM FOLDER game DI FILE game.py
from utils.validator import input_angka # MENGAMBIL FUNGSI input_angka DARI DALAM FOLDER utils DI FILE validator

def menu_utama(): # MEMBUAT SEBUAH FUNGSI PENAMPUNG BERNAMA menu_utama UNTUK MENAMPILKAN MENU PERMAINAN
    while True: # MULAI PROSES PERULANGAN SECARA TERUS-MENERUS SELAMA KONDISI MASIH BERNILAI TRUE
        # TAMPILAN AWAL KETIKA INGIN MEMAINKAN GAME NYA
        print("\n======================================")
        print("        GAME SUIT BALAP KARTU         ")
        print(" ----- ----- ----- ----- ----- -----  ")
        print(" | 1 | | 2 | | 3 | | 4 | | 5 | | 6 |  ")
        print(" ----- ----- ----- ----- ----- -----  ")
        print("======================================")
        print("1. LOGIN & MAIN")
        print("2. REGISTER")
        print("3. LEADERBOARD")
        print("4. RIWAYAT HISTORY")
        print("5. NAVIGASI HISTORY ")
        print("6. KELUAR")
        print("======================================")

        print("\nSILAHKAN REGISTER TERLEBIH DAHULU JIKA BELUM MENDAFTARKAN AKUN!")  # MENAMPILKAN KETERANGAN JIKA BELUM MENDAFTAR AKUN

        pilihan = input_angka("Masukkan pilihan : ") # MEMINTA INPUT ANGKA DARI PENGGUNA DAN MENYIMPANNYA KE VARIABEL pilihan MENGGUNAKAN FUNGSI validator

        if pilihan == 1: # JIKA MEMILIH MENU 1
            gmail_login = login() # MAKA JALANKAN FUNGSI login DAN MENYIMPAN HASILNYA
            if gmail_login: # JIKA DATA YANG DIMASUKKAN KETIKA LOGIN TADI ADA DI DALAM FILE
                mulai_game(gmail_login, history_game, history_double) # MAKA JALANKAN FUNGSI mulai_game DENGAN MEMBAWA DATA LOGIN, TEMPAT single list, DAN double list

        elif pilihan == 2: # JIKA MEMILIH MENU 2
            register() # MAKA JALANKAN FUNGSI register

        elif pilihan == 3: # JIKA MEMILIH MENU 3
            leaderboard() # MAKA JALANKAN FUNGSI leaderboard

        elif pilihan == 4: # JIKA MEMILIH MENU 4
            # TAMPILKAN JUDUL DAN SUB JUDUL RIWAYAT KARTU
            print("\n========== HASIL PEMILIHAN KARTU ===========") 
            print("===== (pada satu permainan sebelumnya) =====\n")
            history_game.tampilkan_history() # MEMANGGIL FUNGSI DARI OBJEK SingleLinkedList UNTUK MENAMPILKAN SEMUA RIWAYAT DATA

        elif pilihan == 5: # JIKA PILIHAN 5
            while True: # MULAI PROSES PERULANGAN SECARA TERUS-MENERUS SELAMA KONDISI MASIH BERNILAI TRUE
                print("\n===== DOUBLE LINKED LIST =====") # TAMPILKAN JUDUL MENU DOUBLE LINKED LIST
                # TAMPILKAN MENU MENU NYA
                print("1. Lihat History Sekarang")
                print("2. Next History")
                print("3. Previous History")
                print("4. Kembali")

                pilih = input("Masukkan pilihan : ") # MEMINTA INPUT ANGKA DARI PENGGUNA UNTUK MEMILIH MENU NYA

                if pilih == "1": # JIKA PILIH 1 
                    history_double.tampilkan_current() # MAKA MEMANGGIL FUNGSI OBJEK DoubleLinkedList UNTUK MELIHAT DATA YANG DITUNJUK SAAT INI
                elif pilih == "2": # JIKA PILIH 2
                    history_double.next_history() # MEMANGGIL FUNGSI OBJEK DoubleLinkedList UNTUK MENGGESER PENUNJUK KE DATA BERIKUTNYA
                elif pilih == "3": # JIKA PILIH 3
                    history_double.prev_history() # MEMANGGIL FUNGSI OBJEK DoubleLinkedList UNTUK MENGGESER PENUNJUK KE DATA SEBELUMNYA
                elif pilih == "4": # JIKA PILIH 4
                    break # HENTIKAN PERULANGAN DAN KEMBALI KE MENU SEBELUMNYA
                else: # JIKA INPUTAN YANG DIMASUKKAN SELAIN 1, 2, 3, 4
                    print("Pilihan tidak tersedia!") # MAKA TAMPILKAN PESAN

        elif pilihan == 6: # JIKA PILIH 6
            print("\nTerima kasih telah bermain!") # MAKA TAMPILKAN PESAN
            break # HENTIKAN PERULANGAN DAN KEMBALI KE MENU SEBELUMNYA
 
        else: # JIKA INPUTAN YANG SIMASUKKAN PADA MENU AWAL GAME SELAIN 1, 2, 3, 4, 5, 6
            print("\nPilihan tidak tersedia!") # MAKA TAMPILKAN PESAN
