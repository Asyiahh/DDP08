from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_sisik, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_sisik = warna_sisik
        self.jenis_ikan = jenis_ikan

    def info_ikan(self):
        super().info_animal()
        print("Warna Sisik\t : ", self.warna_sisik,
              "\nJenis Ikan\t : ", self.jenis_ikan)

koi = Ikan("Koi", "Cacing Sutra", "Air", "Bertelur", "Orane dan Putih", "Air Tawar")
koi.info_ikan()
print()
bawal = Ikan("Bawal", "Cacing Sutra", "Air", "Bertelur", "Abu-abu", "Air Tawar")
bawal.info_ikan()