from ClassData import DataMahasiswa

class processdatamahasiswa: 
    def __init__(self):
        self.daftar_mahasiswa = []
    def Tambah_Mahasiswa(self, nama, nim, nilai):
        if not isinstance(nilai, (int, float)):
            raise ValueError("nilai harus berupa angka")
        if nilai < 0 or nilai > 100:
            raise ValueError
        mhs = DataMahasiswa(nama, nim, nilai)
        self.daftar_mahasiswa.append(mhs)

def rata_rata(self):
    if len(self.daftar_mahasiswa) == 0:
        return 0
    total = sum(m.nilai for m in self.daftar_mahasiwa)

    return total / len(self.daftar_mahasiswa)