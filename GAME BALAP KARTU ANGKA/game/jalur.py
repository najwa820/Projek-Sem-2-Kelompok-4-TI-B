from utils.constants import PANJANG_JALUR

def tampilkan_jalur(posisi, simbol):    #Untuk menampilkan posisi player atau komputer 
    kiri = "=" * posisi #Bagian kiri jalur dari posisi saat ini
    kanan = "=" * (PANJANG_JALUR - posisi)  #Bagian kanan jalur dari sisa panjang jalur
    print(f"{kiri}{simbol}{kanan}") #Menampilkan simbol player atau komputer di posisinya

def cek_menang(player, komputer):   #Menentukan pemenang berdasarkan kartu yang dimainkan
    if player == 1 and komputer == 6:   #Aturan permainan
        return True
    if player == 6 and komputer == 1:   #Aturan permainan
        return False
    return player > komputer    #Selain aturan diatas kartu yg lebih besar menang