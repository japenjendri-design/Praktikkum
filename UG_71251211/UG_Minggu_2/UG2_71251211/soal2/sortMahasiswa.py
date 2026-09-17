import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    if index not in maps:
        print("Index tidak valid!")
        return
    kolom = maps[index]
    n = len(data)

    # Kerjakan disini
    for i in range(n - 1):
        for j in range(n - 1 - i):

            if rev == False:

                if data[j][kolom] > data[j + 1][kolom]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:

                if data[j][kolom] < data[j + 1][kolom]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
