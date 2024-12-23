from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal(),
        print("Paruh\t\t : ", self.paruh,
              "\nWarna Bulu\t : ", self.warna_bulu)
        
Burung_beo = Burung("Beo", "Jagung", "Darat", "Bertelur", "melengkung", "Warna warni")
Burung_beo.info_burung()
print()
Burung_gagak = Burung("Gagak", "Bangkai", "Hutan", "Bertelur", "Runcing", "Hitam")
Burung_gagak.info_burung()