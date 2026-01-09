from class_process import ProcessMahasiswa

class ViewMahasiswa:
    def __init__(self):
        self.proses = ProcessMahasiswa()

    def input_data(self):
        while True:
            try:
                nama = input("masukan nama anda: ")
                nim = input("Masukan NIM: ")
                nilai = float(input("masukan nilai (0-100): "))
                self.proses.tambah_mahasiswa(nama, nim, nilai)
            except ValueError as e:
                print("error", e)
            lanjut = input("tambah data lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

    def tampil_data(self):
        print("\nDaftar Mahasiswa")
        print("{:<5} {:<20} {:<15} {:<5}".format("No", "Nama" "NIM", "Nilai"))
        for i, m in enumerate(self.proses.daftar_mahasiswa, start=1):
            print ("{:<5} {:<20} {:<15} {:<5}".format(i, m.nama, m.nim, m.nilai))
        print("Rata-rata Nilai:", self.proses.rata_rata())