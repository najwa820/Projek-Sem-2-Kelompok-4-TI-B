def baca_file(nama_file): # Untuk membaca isi file
    try:
        with open(nama_file, "r") as file: # r = read = baca
            return file.readlines()
    except FileNotFoundError:
        return []

def tulis_file(nama_file, data): # Untuk menulis data terbaru/update
    with open(nama_file, "w") as file: # w = write = tulis
        file.writelines(data)

def tambah_file(nama_file, data): # Untuk menambagkan data ke file
    with open(nama_file, "a") as file: # a = append = tambah
        file.write(data)