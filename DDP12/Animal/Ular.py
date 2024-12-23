from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bisa, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bisa = jenis_bisa
        self.jenis_ular = jenis_ular
        
    def info_ular(self):
        super().info_animal()
        print("Warna kulit\t : ", self.jenis_bisa,
              "\nJenis ular\t : ", self.jenis_ular)

sanca = Ular("Sanca", "Reptil", "Air", "Bertelur", "Tidak Berbisa", "Sanca Hijau")
sanca.info_ular()
print()
kobra = Ular("Korba", "Kadal", "Darat", "Bertelur", "Neurotoxin", "Kaca Tunggal")
kobra.info_ular()