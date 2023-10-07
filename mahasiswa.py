class mahasiswa():

    def __init__(self, npm : int, first_name, last_name, birth_date : int, jurusan, fakultas):
        self.npm = npm
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.fullname = self.first_name + " " + self.last_name
        self.umur = 2023 - int(self.birth_date)

    def full_name(self):
        print(self.fullname)

    def umur_mahasiswa(self):
        print(self.umur)

    def data_lengkap(self):
        print(f"NPM: {self.npm}")
        print(f"Nama: {self.fullname}")
        print(f"Umur: {self.umur}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Jurusan: {self.jurusan}")


mahasiswa_1 = mahasiswa(2306228283, "Nabil Rakaiza", "Abror", "2005", "Sistem Informasi", "Fasilkom")
mahasiswa_2 = mahasiswa(2206228283, "Bambang", "Supriyanto", "1987", "Pendidikan Kedokteran", "FK")

mahasiswa_1.data_lengkap()
print()
mahasiswa_2.data_lengkap()
