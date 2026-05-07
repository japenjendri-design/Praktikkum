def KoalaSorting(a):
    hasil = {}
    
    for item in a:
        for nama, detail in item.items():
            
            # cek apakah ada key "tipe"
            if "tipe" in detail:
                tipe = detail["tipe"]
            else:
                tipe = "unknown"
            
            # kalau tipe belum ada di dictionary
            if tipe not in hasil:
                hasil[tipe] = []
            
            # masukkan nama item
            hasil[tipe].append(nama)
    
    return hasil
