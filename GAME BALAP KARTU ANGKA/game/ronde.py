from game.jalur import cek_menang

def mainkan_ronde(player, komputer):    #hasil ronde permainan
    if player == komputer:  #kalau player dan komputer sama
        return "SERI"
    if cek_menang(player, komputer):    #kalau player menang
        return "PLAYER"
    return "KOMPUTER"   #kalau komputer menang