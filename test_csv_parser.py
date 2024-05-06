from csv_management import parse_csv_file
print(parse_csv_file("csv folder\item_inventory.csv"))
print("Pogger")

def my_strip(s, chars=None):
    """
    Menghilangkan simbol spesifik dari string yang dimasukkan

    Input:
        s (str): String yang belum difilter.
        chars (str, opsional): simbol yang dihilangkan, diset None secara standar

    Output:
        str: String yang sudah difilter.
    """
    if chars is None: # Jika memenuhi maka akan otomatis jadi spasi dan karakter whitespace lainnya
        chars = ' \t\n\r\v\f' 

    start = 0
    end = len(s) - 1
    
    # Mencari indeks pertama dari karakter yang bukan merupakan karakter yang harus dihilangkan.
    # 
    while start <= end and s[start] in chars:
        start += 1
    
    # Find the end index of the non-stripped character
    while end >= start and s[end] in chars:
        end -= 1
