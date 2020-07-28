"""
MODULARISASI DASAR MENGHITUNG LUAS SEGITIGA
luas segitiga = alas*tinggi/2
"""

print('perhitungan sederhana luas segitiga tanpa fungsi')
alas = 24
tinggi = 30
luas = alas * tinggi / 2
print(f'\nSegitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas = {luas}')


def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


print(f'menghitung luas segitiga memakai fungsi = {hitung_luas_segitiga(10, 7)}')
print(f'menghitung luas segitiga memakai fungsi = {hitung_luas_segitiga(14, 7)}')


def hitung_luas_tanah(panjang, lebar):
    luas_tanah = panjang * lebar
    return luas_tanah


print(f'\nluas tanah mang Ujang = {hitung_luas_tanah(97, 34)} meter persegi')
print(f'luas tanah mang Asep = {hitung_luas_tanah(97, 34)} meter persegi')

print('\nBelajar menghitung luas tanah segitiga')
sisi_a = 12
sisi_b = 15
sisi_c = 66
luas_keliling_tanah_segitga = sisi_a + sisi_b + sisi_c / 2
luas_tanah_segitiga = luas_keliling_tanah_segitga * ((luas_keliling_tanah_segitga - sisi_a) * (luas_keliling_tanah_segitga - sisi_b) * (luas_keliling_tanah_segitga - sisi_c) )

print(f'luas tanah segitiga adalah = {luas_tanah_segitiga}')
