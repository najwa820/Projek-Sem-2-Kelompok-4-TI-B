#========================================
#Penerapan materi Graph (matkul strukdat)
#========================================

class Graph:
    def __init__(self):
        self.data = {}

    def tambah_relasi(self, player, komputer):
        # KALAU ANGKA PLAYER BELUM ADA
        if player not in self.data:
            self.data[player] = []

        # TAMBAHKAN LAWAN
        self.data[player].append(komputer)

    def tampilkan_graph(self):
        print("\n===== RIWAYAT PERTANDINGAN ANGKA =====")
        for player in self.data:
            print(f"{player} melawan {self.data[player]}")