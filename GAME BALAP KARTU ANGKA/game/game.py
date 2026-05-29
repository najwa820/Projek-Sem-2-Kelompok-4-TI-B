import random # Untuk memilih angka komputer secara acak

from game.kartu import Kartu
from game.jalur import tampilkan_jalur, PANJANG_JALUR
from game.ronde import mainkan_ronde
from game.menu_game import tampilkan_menu_akhir
from tree import TreeNode
from graph import Graph

from user.leaderboard import leaderboard, tambah_skor

from history.stack import Stack

from utils.validator import input_angka
from utils.constants import KODE_HISTORY

stack = Stack()
graph_game = Graph()

def reset_game():
    return 0, 0, Kartu(), Kartu()

def tampilkan_status(player_pos, komputer_pos, kartu_player):
    print("\nPLAYER")
    tampilkan_jalur(player_pos, "P")

    print("\nCOMPUTER")
    tampilkan_jalur(komputer_pos, "C")

    print(f"\nKartu tersedia : {kartu_player.tampilkan()}")
    print("Ketik 0 untuk melihat kartu yang sudah dipilih dan posisi sebelumnya")

def input_player(kartu_player):
    while True:
        angka = input_angka("\nMasukkan angka : ")
        if angka == KODE_HISTORY:
            stack.tampilkan()
            continue
        if not kartu_player.tersedia(angka):
            print("Angka tidak tersedia!")
            continue
        return angka

def mulai_game(gmail_login, history_game, history_double):
    player_pos, komputer_pos, kartu_player, kartu_komputer = reset_game()
    while True:
        tampilkan_status(player_pos, komputer_pos, kartu_player)
        player = input_player(kartu_player)
        komputer = random.choice(kartu_komputer.tampilkan())

        print(f"\nComputer memilih : {komputer}")

        kartu_player.gunakan(player)
        kartu_komputer.gunakan(komputer)

        old_player = player_pos
        old_komputer = komputer_pos

        hasil = mainkan_ronde(player, komputer)
        graph_game.tambah_relasi(player, komputer)

        if hasil == "SERI":
            print("\nHASIL SERI!")

            history_game.tambah_history("HASIL SERI")
            history_double.tambah_history("HASIL SERI")

        elif hasil == "PLAYER":
            print("\nPLAYER MENANG!")
            print(f"Maju {player} langkah!")

            history_game.tambah_history("PLAYER MENANG")
            history_double.tambah_history("PLAYER MENANG")

            player_pos += player

        else:
            print("\nCOMPUTER MENANG!")
            print(f"Maju {komputer} langkah!")

            history_game.tambah_history("COMPUTER MENANG")
            history_double.tambah_history("COMPUTER MENANG")

            komputer_pos += komputer

        stack.push(player, komputer, old_player, old_komputer)

        if player_pos > PANJANG_JALUR:
            player_pos = PANJANG_JALUR

        if komputer_pos > PANJANG_JALUR:
            komputer_pos = PANJANG_JALUR

        if len(kartu_player.tampilkan()) == 0:
            kartu_player.reset()
            print("\nKartu PLAYER di-reset!")

        if len(kartu_komputer.tampilkan()) == 0:
            kartu_komputer.reset()
            print("Kartu COMPUTER di-reset!")

        # =====================
        # PENERAPAN MATERI TREE
        # =====================

        # ROOT
        game_tree = TreeNode("Game")

        # PLAYER
        player_node = TreeNode("Player")
        player_posisi = TreeNode(f"Posisi : {player_pos}")
        player_kartu = TreeNode(f"Kartu : {kartu_player.tampilkan()}")

        player_node.tambah_bagian(player_posisi)
        player_node.tambah_bagian(player_kartu)

        # KOMPUTER
        komputer_node = TreeNode("Komputer")
        komputer_posisi = TreeNode(f"Posisi : {komputer_pos}")
        komputer_kartu = TreeNode(f"Kartu : {kartu_komputer.tampilkan()}")

        komputer_node.tambah_bagian(komputer_posisi)
        komputer_node.tambah_bagian(komputer_kartu)

        # MASUK KE GAME
        game_tree.tambah_bagian(player_node)
        game_tree.tambah_bagian(komputer_node)

        #TAMPILKAN TREE
        print("\n=== STRUKTUR TREE GAME ===")
        game_tree.tampilkan()

        selesai = False

        if player_pos >= PANJANG_JALUR:
            print("\nPLAYER MENANG GAME!")
            hasil_skor = tambah_skor(gmail_login)
            print(f"SKOR KAMU : {hasil_skor}")
            selesai = True

        elif komputer_pos >= PANJANG_JALUR:
            print("\nCOMPUTER MENANG GAME!")
            selesai = True

        while selesai:
            tampilkan_menu_akhir()
            pilihan = input("\nMasukkan pilihan : ")
            if pilihan == "1":
                player_pos, komputer_pos, kartu_player, kartu_komputer = reset_game()
                print("\nGAME DIMULAI ULANG!")
                break
            elif pilihan == "2":
                leaderboard()
            elif pilihan == "3":
                print("\n===== HISTORY PERMAINAN =====")
                history_game.tampilkan_history()
            elif pilihan == "4":
                graph_game.tampilkan_graph()
            elif pilihan == "5":
                return  
            else:
                print("Pilihan tidak tersedia!")