def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    if current_length == 0:
        return [current_value]

    if current_value >= sorted_array[current_length - 1]:
        return sorted_array + [current_value]
    
    last_value = sorted_array[current_length - 1]
    remaining_array = sorted_array[:current_length - 1]

    result = InsertRecursive(
        remaining_array,
        current_value,
        current_length - 1
                             )

    return result + [last_value]



def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.
    if current_length == 0:
        return[]

    current_value = data_array[current_length - 1]

    result = RecursiveFilterSort(
        data_array,
        current_length - 1
    )

    if current_value % 2 != 0:
        return InsertRecursive(
            result,
            current_value,
            len(result)
        )
    return result



# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0] 
NIM_MAHASISWA = "71251211"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 3: cetak hasil akhir sesuai format yang diminta.
    print("=====  FILTER & SORT NIM  ======")
    print("NIM              :", NIM_MAHASISWA)
    print("Tipe             : GANJIL (Ascending)")
    print("Data Digit Awal  :", raw_data)
    print("Hasil            :", final_result)

