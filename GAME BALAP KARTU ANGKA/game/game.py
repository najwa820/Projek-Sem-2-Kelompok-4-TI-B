import random # Mengambil pustaka bawaan Python untuk mengacak nilai (misal: pilihan komputer)

from game.kartu import Kartu # MENGAMBIL CETAKAN class Kartu DARI FOLDER game
from game.jalur import tampilkan_jalur, PANJANG_JALUR # MENGAMBIL FUNGSI tampilkan_jalur DAN BATAS PANJANG LINTASAN DARI FILE jalur.py
from game.ronde import mainkan_ronde # MENGAMBIL FUNGSI mainkan_ronde DARI DALAM FOLDER game DI FILE ronde.py
from tree import TreeNode # MENGAMBIL CETAKAN class TreeNode DARI FOLDER game
from graph import Graph # MENGAMBIL CETAKAN class Graph DARI FOLDER game

from user.leaderboard import leaderboard, tambah_skor # MENGAMBIL FUNGSI PENAMPILAN DAN PENAMBAHAN SKOR PLAYER DARI FILE leaderboard.py

from history.stack import Stack # MENGAMBIL CETAKAN class Stack DARI FOLDER history 

from utils.validator import input_angka # MENGAMBIL FUNGSI input_angka DARI DALAM FOLDER utils DI FILE validator.py
from utils.constants import KODE_HISTORY # MENGAMBIL KONSTANTA ANGKA KHUSUS UNTUK MENDETEKSI PERINTAH CEK RIWAYAT

stack = Stack() # MEMBUAT OBJEK stack BARU SEBAGAI TEMPAT MENYIMPAN RIWAYAT PERMAINAN YANG BISA DITUMPUK
graph_game = Graph() # MEMBUAT OBJEK graph BARU UNTUK MEMETAKAN HUBUNGAN PERTARUNGAN ANTAR KARTU PLAYER VS KOMPUTER

def reset_game(): # MEMBUAT FUNGSI reset_game UNTUK MENGEMBALIKAN POSISI KE NOL DAN MEMPERBARUI OBJEK KARTU BARU
    return 0, 0, Kartu(), Kartu() # MENGEMBALIKAN EMPAT NILAI: POSISI PLAYER 0, POSISI KOMPUTER 0, OBJEK Kartu PLAYER BARU, OBJEK Kartu KOMPUTER BARU

def tampilkan_status(player_pos, komputer_pos, kartu_player): # MEMBUAT FUNGSI UNTUK MENCETAK VISUALISASI LINTASAN DAN DAFTAR KARTU YANG DIPEGANG PLAYER SAAT INI
    print("\nPLAYER") # MENAMPILKAN KETERANGAN PLAYER
    tampilkan_jalur(player_pos, "P") # MEMANGGIL FUNGSI tampilkan_jalur DENGAN POSISI MILIK PLAYER BERTANDA HURUF 'P'

    print("\nCOMPUTER") # MENAMPILKAN KETERANGAN KOMPUTER
    tampilkan_jalur(komputer_pos, "C") # MEMANGGIL FUNGSI tampilkan_jalur DENGAN POSISI MILIK KOMPUTER BERTANDA HURUF 'C'

    print(f"\nKartu tersedia : {kartu_player.tampilkan()}") # MENCETAK DAFTAR KARTU ANGKA YANG SAAT INI MASIH BISA DIPILIH OLEH PLAYER LEWAT FUNGSI tampilkan
    print("Ketik 0 untuk melihat kartu yang sudah dipilih dan posisi sebelumnya") # MENAMPILKAN KETERANGAN UNTUK MELIHAT KARTU YANG DIPILIH DAN POSISI SEBELUMNYA

def input_player(kartu_player): # # MEMBUAT FUNGSI PENERIMA INPUT DARI PLAYER DAN MEMASTIKAN KARTU YANG DIPILIH VALID ATAU TERSEDIA
    while True: # MULAI PROSES PERULANGAN SECARA TERUS-MENERUS SELAMA KONDISI MASIH BERNILAI TRUE
        angka = input_angka("\nMasukkan angka : ") # MEMINTA INPUT ANGKA TER-VALIDASI DARI PLAYER DAN DISIMPAN DI VARIABEL 'angka' LEWAT FUNGSI input_angka
        if angka == KODE_HISTORY: # MEMERIKSA APAKAH ANGKA YANG DIMASUKKAN ADALAH KODE RAHASIA KODE_HISTORY (ANGKA 0)
            stack.tampilkan() # MENAMPILKAN ISI TUMPUKAN RIWAYAT PERMAINAN SAAT INI LEWAT FUNGSI tampilkan PADA OBJEK stack
            continue # MENGULANG KEMBALI KE ATAS LOOP UNTUK MEMINTA INPUT ANGKA KARTU SESUNGGUHNYA
        if not kartu_player.tersedia(angka): # MEMERIKSA JIKA ANGKA KARTU YANG DIMASUKKAN TIDAK ADA DI DAFTAR KARTU MILIKNYA LEWAT FUNGSI tersedia
            print("Kartu angka tidak tersedia!") # TAMPILKAN PESAN JIKA KARTU ANGKA YANG DIPILIH TIDAK ADA
            continue # MENGULANG LOOP KE ATAS UNTUK MEMINTA INPUT ULANG ANGKA KARTU
        return angka # 

def mulai_game(gmail_login, history_game, history_double): # MEMBUAT FUNGSI INTI mulai_game YANG MENGATUR JALANNYA RONDE, LINKED LIST, TREE, GRAPH, HINGGA SELESAI
    player_pos, komputer_pos, kartu_player, kartu_komputer = reset_game() # MENYIAPKAN VARIABEL AWAL PERMAINAN LEWAT FUNGSI reset_game
    while True: # MELAKUKAN PERULANGAN TERUS-MENERUS SEPANJANG JALANNYA GAME (RONDE DEMI RONDE)
        tampilkan_status(player_pos, komputer_pos, kartu_player) # MENAMPILKAN STATUS LINTASAN POSISI DAN SISA KARTU DI AWAL RONDE LEWAT FUNGSI tampilkan_status
        player = input_player(kartu_player) # MENJALANKAN FUNGSI input_player UNTUK MENDAPATKAN PILIHAN KARTU DARI PLAYER
        komputer = random.choice(kartu_komputer.tampilkan()) # KOMPUTER MEMILIH KARTU SECARA ACAK DARI DAFTAR SISA KARTUNYA MENGGUNAKAN PUSTAKA random DAN FUNGSI tampilkan

        print(f"\nComputer memilih : {komputer}") # MENCETAK KARTU ANGKA YANG DIPILIH OLEH KOMPUTER KE LAYAR TERMINAL

        kartu_player.gunakan(player) # MENGUBAH STATUS KARTU PILIHAN PLAYER MENJADI HANGUS/TERPAKAI LEWAT FUNGSI gunakan
        kartu_komputer.gunakan(komputer) # MENGUBAH STATUS KARTU PILIHAN KOMPUTER MENJADI HANGUS/TERPAKAI LEWAT FUNGSI gunakan

        old_player = player_pos # MENYIMPAN POSISI PLAYER SAAT INI KE VARIABEL SEMENTARA SEBELUM POSISINYA BERUBAH
        old_komputer = komputer_pos # MENYIMPAN POSISI KOMPUTER SAAT INI KE VARIABEL SEMENTARA SEBELUM POSISINYA BERUBAH

        hasil = mainkan_ronde(player, komputer) # MENGADU KARTU PLAYER DAN KOMPUTER LEWAT FUNGSI mainkan_ronde UNTUK MENENTUAKAN PEMENANG RONDE
        graph_game.tambah_relasi(player, komputer) # MENCATAT HUBUNGAN PERTARUNGAN ANTARA KARTU LEWAT FUNGSI tambah_relasi PADA OBJEK graph_game

        if hasil == "SERI": # JIKA HASIL ADALAH "SERI"
            print("\nHASIL SERI!") # MAKA TAMPILKAN "HASIL SERI!"

            history_game.tambah_history("HASIL SERI") # MENAMBAH CATATAN HISTORY BARU LEWAT FUNGSI tambah_history PADA OBJEK history_game
            history_double.tambah_history("HASIL SERI") # MENAMBAH CATATAN HISTORY BARU LEWAT FUNGSI tambah_history PADA OBJEK history_double

        elif hasil == "PLAYER": # JIKA HASIL ADALAH "PLAYER"
            print("\nPLAYER MENANG!") # MAKA TAMPILKAN "PLAYER MENANG"
            print(f"Maju {player} langkah!") # CENCETAK JUMLAH LANGKAH MAJU BERDASARKAN ANGKA KARTU YANG DIGUNAKAN PLAYER

            history_game.tambah_history("PLAYER MENANG") # MENAMBAH CATATAN "PLAYER MENANG" LEWAT FUNGSI tambah_history PADA OBJEK history_game
            history_double.tambah_history("PLAYER MENANG") # MENAMBAH CATATAN "PLAYER MENANG" LEWAT FUNGSI tambah_history PADA OBJEK history_double

            player_pos += player # TAMBAHKAN KOORDINAT POSISI PLAYER SEJAUH NILAI KARTU YANG IA MAINKAN

        else: # SELAIN DARI PILIHAN DIATAS, MAKA
            print("\nCOMPUTER MENANG!") # TAMPILKAN COMPUTER MENANG
            print(f"Maju {komputer} langkah!") # CENCETAK JUMLAH LANGKAH MAJU BERDASARKAN ANGKA KARTU YANG DIGUNAKAN KOMPUTER 

            history_game.tambah_history("COMPUTER MENANG") # MENAMBAH CATATAN "COMPUTER MENANG" LEWAT FUNGSI tambah_history PADA OBJEK history_game
            history_double.tambah_history("COMPUTER MENANG") # MENAMBAH CATATAN "COMPUTER MENANG" LEWAT FUNGSI tambah_history PADA OBJEK history_double

            komputer_pos += komputer # TAMBAHKAN KOORDINAT POSISI KOMPUTER SEJAUH NILAI KARTU YANG IA MAINKAN

        stack.push(player, komputer, old_player, old_komputer) # MEMASUKKAN PAKET DATA RONDE INI KE PUNCAK TUMPUKAN OBJEK stack LEWAT FUNGSI push

        if player_pos > PANJANG_JALUR: # JIKA POSISI PLAYER LEBIH BESAR DARI PANJANG_JALAUR
            player_pos = PANJANG_JALUR # MAKA BUAT POSISI PLAYER AGAR TETAP PAS BERADA DI ANGKA BATAS PANJANG_JALUR

        if komputer_pos > PANJANG_JALUR: # JIKA POSISI KOMPUTER LEBIH BESAR DARI PANJANG_JALAUR
            komputer_pos = PANJANG_JALUR # MAKA BUAT POSISI KOMPUTER AGAR TETAP PAS BERADA DI ANGKA BATAS PANJANG_JALUR

        if len(kartu_player.tampilkan()) == 0: # JIKA SELURUH KARTU DI TANGAN PLAYER SUDAH HABIS
            kartu_player.reset() # ISI ULANG KEMBALI SELURUH KARTU PLAYER KE KONDISI AWAL LEWAT FUNGSI reset
            print("\nKartu PLAYER di-reset!") # TAMPILKAN "Kartu PLAYER di-reset!"

        if len(kartu_komputer.tampilkan()) == 0: # JIKA SELURUH KARTU DI TANGAN KOMPUTER SUDAH HABIS
            kartu_komputer.reset() # ISI ULANG KEMBALI SELURUH KARTU PLAYER KE KONDISI AWAL LEWAT FUNGSI reset
            print("Kartu COMPUTER di-reset!") # TAMPILKAN "Kartu COMPUTER di-reset!"

        # =====================================
        # PENERAPAN MATERI TREE (STRUKTUR DATA)
        # =====================================

        # ROOT
        game_tree = TreeNode("Game") # BUAT BAGIAN POHON UTAMA (ROOT NODE) BERAMA "Game" MENGGUNAKAN CETAKAN TreeNode

        # PLAYER
        player_node = TreeNode("Player") # BUAT CABANG NODE BARU UNTUK MENAMPUNG DATA KELOMPOK "Player" MENGGUNAKAN CETAKAN TreeNode
        player_posisi = TreeNode(f"Posisi : {player_pos}") # BUAT SEPERTI DAUN NODE YANG BERISI STRING INFO POSISI TERKINI DARI PLAYER
        player_kartu = TreeNode(f"Kartu : {kartu_player.tampilkan()}") # BUAT SEPERTI DAUN NODE YANG BERISI STRING DAFTAR SISA KARTU MILIK PLAYER LEWAT FUNGSI tampilkan

        player_node.tambah_bagian(player_posisi) # KAITKAN NODE INFORMASI POSISI KE DALAM KELOMPOK NODE "Player" LEWAT FUNGSI tambah_bagian
        player_node.tambah_bagian(player_kartu) # KAITKAN NODE INFORMASI POSISI KE DALAM KELOMPOK NODE "Player" LEWAT FUNGSI tambah_bagian

        # KOMPUTER
        komputer_node = TreeNode("Komputer") # BUAT CABANG NODE BARU UNTUK MENAMPUNG DATA KELOMPOK "Komputer" MENGGUNAKAN CETAKAN TreeNode
        komputer_posisi = TreeNode(f"Posisi : {komputer_pos}") # BUAT SEPERTI DAUN NODE YANG BERISI STRING INFO POSISI TERKINI DARI KOMPUTER
        komputer_kartu = TreeNode(f"Kartu : {kartu_komputer.tampilkan()}") # BUAT SEPERTI DAUN NODE YANG BERISI STRING DAFTAR SISA KARTU MILIK KOMPUTER LEWAT FUNGSI tampilkan

        komputer_node.tambah_bagian(komputer_posisi) # KAITKAN NODE INFORMASI POSISI KE DALAM KELOMPOK NODE "Komputer" LEWAT FUNGSI tambah_bagian
        komputer_node.tambah_bagian(komputer_kartu) # KAITKAN NODE INFORMASI POSISI KE DALAM KELOMPOK NODE "Komputer" LEWAT FUNGSI tambah_bagian

        # MASUK KE GAME
        game_tree.tambah_bagian(player_node) # MEMASUKKAN SELURUH PAKET NODE "Player" KE BAWAH NAUNGAN BAGIAN POHON UTAMA "Game" LEWAT FUNGSI tambah_bagian
        game_tree.tambah_bagian(komputer_node) # MEMASUKKAN SELURUH PAKET NODE "Komputer" KE BAWAH NAUNGAN BAGIAN POHON UTAMA "Game" LEWAT FUNGSI tambah_bagian

        #TAMPILKAN TREE
        print("\n=== STRUKTUR TREE GAME ===") # TAMPILKAN "=== STRUKTUR TREE GAME ==="
        game_tree.tampilkan() # MEMANGGIL FUNGSI tampilkan PADA OBJEK POHON game_tree UNTUK MENCETAK VISUAL STRUKTUR DATANYA

        selesai = False # MEMBUAT PENANDA AWAL KALAU PERMAINAN BELUM SELESAI SEPENUHNYA

        if player_pos >= PANJANG_JALUR: # JIKA POSISI PLAYER LEBIH BESAR SAMA DENGAN PANJANG_JALAUR
            print("\nPLAYER MENANG GAME!") # MAKA TAMPILKAN "PLAYER MENANG GAME!"
            hasil_skor = tambah_skor(gmail_login) # MENAMBAHKAN SKOR KEMENANGAN KE PENYIMPANAN AKUN LEWAT FUNGSI tambah_skor BERDASARKAN gmail_login NYA
            print(f"SKOR KAMU : {hasil_skor}") # TAMPILKAN SKOR PEMAIN
            selesai = True # UBAH STATUS PENANDA PERMAINAN MENJADI True (PERMAINAN RESMI BERAKHIR)

        elif komputer_pos >= PANJANG_JALUR: # JIKA POSISI KOMPUTER LEBIH BESAR SAMA DENGAN PANJANG_JALAUR
            print("\nCOMPUTER MENANG GAME!") # MAKA TAMPILKAN "COMPUTER MENANG GAME!"
            selesai = True # UBAH STATUS PENANDA PERMAINAN MENJADI True (PERMAINAN RESMI BERAKHIR)

        while selesai: # LAKUKAN PERULANGAN AKHOR UNTUK MENU AKHIR GAME JIKA KONDISI VARIABEL 'selesai' BERNILAI True
            # TAMPILKAN MENU MENU NYA
            print("\n1. Main Lagi")
            print("2. Leaderboard")
            print("3. Lihat History")
            print("4. Lihat Riwayat Pertandingan Angka")
            print("5. Kembali ke Menu")

            pilihan = input("\nMasukkan pilihan : ") # INPUT ANGKA DARI PENGGUNA DAN MENYIMPANNYA KE VARIABEL pilihan
            if pilihan == "1": # JIKA PILIHAN ADALAH "1"
                player_pos, komputer_pos, kartu_player, kartu_komputer = reset_game() # KOSONGKAN ULANG DATA POSISI DAN KARTU MENGGUNAKAN FUNGSI reset_game
                print("\nGAME DIMULAI ULANG!") # TAMPILKAN "GAME DIMULAI ULANG!"
                break # BERHENTIKAN LOOP MENU AKHIR DAN KEMBALI MASUK KE LOOP RONDE GAME UTAMA
            elif pilihan == "2": # JIKA PILIHAN ADALAH "2"
                leaderboard() # MEMANGGIL FUNGSI leaderboard UNTUK MENAMPILKAN URUTAN PERINGKAT SKOR PEMAIN LAIN
            elif pilihan == "3": # JIKA PILIHAN ADALAH "3"
                print("\n===== HISTORY PERMAINAN =====") # TAMPILKAN "===== HISTORY PERMAINAN ====="
                history_game.tampilkan_history() # MEMANGGIL FUNGSI tampilkan_history PADA OBJEK history_game UNTUK MENCETAK HASIL RONDE DARI AWAL
            elif pilihan == "4": # JIKA PILIHAN ADALAH "4"
                graph_game.tampilkan_graph() # MEMANGGIL FUNGSI tampilkan_graph PADA OBJEK graph_game UNTUK MENGHUBUNGKAN MATRIKS KARTU
            elif pilihan == "5": # JIKA PILIHAN ADALAH "5"
                return # KELUAR DARI FUNGSI mulai_game DAN KEMBALI KE MENU UTAMA
            else: # JIKA TIDAK ADA PILIHAN SELAIN DI ATAS
                print("Pilihan tidak tersedia!") # MAKA TAMPILKAN "Pilihan tidak tersedia!"
