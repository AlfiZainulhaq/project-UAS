from class_view import ViewMahasiswa

def main():
    view = ViewMahasiswa()
    view.input_data()
    view.tampil_data()

if __name__ == "__main__":
    main()("{:<5} {:<20} {:<15} {:<5}".format("No", "Nama" "NIM", "Nilai"))