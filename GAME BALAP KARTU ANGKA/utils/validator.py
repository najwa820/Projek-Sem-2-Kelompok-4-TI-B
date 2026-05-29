def input_angka(pesan): # untuk meminta input an dari pemain
    while True: # ulang terus hingga valid
        try:
            return int(input(pesan)) # ubah ke bentuk integer
        except ValueError:
            print("Input harus angka!")