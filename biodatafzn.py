biodatafzn

folder_name = 'FauzanNurpadilah'
file_name = 'FauzanNurpadilah.txt'
biodata = """Nama: Fauzan Nurpadilah
Umur: 20 tahun
Alamat: Kp. Legoknyenang Kec. Cidahu Kab. Sukabumi
Pekerjaan: Karyawan
"""

os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, file_name)
with open(file_path, 'w') as file:
    file.write(biodata)

print(f'Folder "{folder_name}" dan file "{file_name}" \n')

print("Biodata")
with open(file_path, 'r') as file:
    isi = file.read()
    print(isi)