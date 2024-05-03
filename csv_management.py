from split_and_strip_function import my_split



def parse_csv_file(file_path, delimiter = ';'):
    """
    Mengonversi file bertipe csv menjadi list of list 

    Input : 
        - filepath(str) : direktori file csv-nya
        - delimiter : Untuk menghilangkan pemisah antar elemen

    Output : 
        list : list of list yang menyatakan kolom dan baris CSV file
    """

# CSV parser function
    result = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                current_row = list(my_split(line, delimiter))
                result.append(current_row)
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error:", str(e))
    return result

def PrintList(x):
    """
    Mengeprint list of list yang didapat dari CSV parser

    Input : List of list

    Output : Isi dari input yang dibuat sedemikian agar menyerupai tabel
    """
    element = x[0][0] # Menjadikan elemen pertama untuk diuji
    column = x[0] # Menghitung berapa kolom dalam setiap baris (Asumsikan setiap baris memiliki kolom yang sama)

    # Menghitung huruf terbanyak dari semua elemen
    for i in range(len(x)):
        for j in range(len(column)):
            if len(str(element)) < len(str(x[i][j])):
                element = x[i][j]
            else:
                continue
    
    # Memberi pembatas agar terlihat seperti tabel berdasarkan huruf terbanyak dari kata yang sudah dicari
    for i in range(len(x)):
        for j in range(len(column)):
            space_terbanyak = len(str(element))
            jumlah_space = ((space_terbanyak - len(str(x[i][j]))) * " ") + " " * 2
            print(x[i][j], end = f'{jumlah_space}|')

        print()
    return ""