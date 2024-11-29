import math

def l_balok(p, l, t):
    hitung = 2 * (p*l)+(p*t)+(l*t)
    print(f'Luas Balok Adalah {hitung}')
    
def l_kubus(sisi):
    hitung = 6 * (sisi * sisi)
    print(f'Luas kubus Adalah {hitung}')
    
def l_tabung(r2, t):
    hitung = 6 * (r2 + t)
    print(f'Luas Tabung Adalah {hitung}')
    
def l_limas(a, st):
    hitung = math.sqrt(3) * a * st
    print(f'Luas Limas Adalah {hitung}')
    
def l_prismasegitiga(a, t, tp):
    hitung = (1/2 * a * t) * tp
    print(f'Luas Prisma Segitiga {hitung}')