# NOMOR 2 : SEGITIGA EXCEL

import xlsxwriter

def segitigaExcel(x):
    book = xlsxwriter.Workbook('soal2.xlsx')
    sheet = book.add_worksheet('Sheet1')
    himpunan_syarat = [1]
    awal = 1
    hasil = ''
    inisiasi = 0
    x = x.replace(' ', '')
    for i in range(2, len(x)):
        awal = awal + i
        himpunan_syarat.append(awal)
    if len(x) in himpunan_syarat :
        for i in range(himpunan_syarat.index(len(x))+2): 
            for j in range(i) :    
                hasil = x[inisiasi]
                inisiasi += 1
                sheet.write(i-1,j, hasil)
    else :
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")
    book.close()

# segitigaExcel('Purwadhika')
# segitigaExcel('Purwadhika Startup and Coding School @BSD')
# segitigaExcel('kode')
segitigaExcel('kode python')
# segitigaExcel('Lintang')



