import math

# Deklarasi 
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'Luas Persegi Adalah {hitung}')
    
def l_persegi_panjang(p, l):
    hitung = p * l
    print(f'Luas Persegi Panjang Adalah {hitung}')
    
def l_segi_tiga(a, t):
    hitung = 1/2 * a * t
    print(f'Luas Segitiga Adalah {hitung}')
    
def l_lingkaran(r):
    hitung = math.pi * r * r
    print(f'Luas Lingkaran Adalah {hitung}')
    
def l_jajar_genjang(a, t):
    hitung = a * t
    print(f'Luas Jajajr Genjang Adalah {hitung}')