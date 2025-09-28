# Mini-Projek-2
## _Sistem Manajemen Pencatatan Hutang (Update)_

Nama: Rivalio Chendra          
NIM: 2509116039      
Kelas: Sistem Informasi A'2025    
<br><br>
AKUN:

-Manager,
Username: admin,
Password: 123

-Karyawan,
username: budak,
password: 111

-Vierwer,
Username: user,
password: 222

### Deskripsi
Program ini adalah update untuk Sistem Manajemen Pencatatan Hutang, yang telah dilengkapi dengan loop dan juga login sebagai role manager yang dapat menggunakan semua CRUD, Karyawan hanya menambah, melihat, dan mengubah, dan yang terakhir adalah viewer yang hanya bisa melihat saja.

### Flowchart Program
<img width="1709" height="1589" alt="Flowchart pencatat hutang-Halaman-1 drawio" src="https://github.com/user-attachments/assets/a5bbde56-22cd-43f6-9df1-b335f0678624" />
<img width="1108" height="1451" alt="Flowchart pencatat hutang-Halaman-2 drawio" src="https://github.com/user-attachments/assets/5d94e21f-a269-4a18-b4ff-8643dd010cd2" />
<img width="718" height="844" alt="Flowchart pencatat hutang-Halaman-3 drawio" src="https://github.com/user-attachments/assets/2e79059b-1006-4528-b25e-9f3eac7b4ef1" />
<br><br>

### Alur Program  
-**Saat Program dijalankan** <br>
Output: <br>

<img width="246" height="59" alt="image" src="https://github.com/user-attachments/assets/68f9cad1-fa37-4e01-a0f6-f1671f74527e" /> <br>
Program akan meminta username dan password. <br><br>
Jika akun yang dimasukan salah, akan keluar output: <br>
<img width="492" height="125" alt="image" src="https://github.com/user-attachments/assets/1aca6826-466f-4b3c-aa4b-f6d0062458a6" /> <br><br>

-**Jika Login berhasil** <br>
Contoh kalau login sebagai admin (role = Manager): <br>
<img width="378" height="315" alt="image" src="https://github.com/user-attachments/assets/40b78cd6-3c4e-4e35-80ca-a1b62baa7b6e" /> <br>
Kalau login budak → Karyawan <br>
Kalau login user → Viewer <br><br>

-**Tampil menu sesuai Role** <br>
*a). kalau manager*:<br>
<img width="397" height="317" alt="image" src="https://github.com/user-attachments/assets/dabfc05f-304e-4d58-bdd1-29a0c81ad05d" /> <br><br>
*b). kalau karyawan*:<br>
<img width="389" height="306" alt="image" src="https://github.com/user-attachments/assets/cd1e41a1-8145-4c55-84b4-e450fdf56232" /> <br><br>
*c). kalau viewer*:<br>
<img width="357" height="241" alt="image" src="https://github.com/user-attachments/assets/9ef5de80-ee64-467b-8a5d-4acd00c87363" /> <br><br>

-**Output dari tiap pilihan menu** <br>
**1. Tambah hutang**<br>
<img width="271" height="200" alt="image" src="https://github.com/user-attachments/assets/cbc20c08-c3ad-4188-b781-64a06709d82b" /> <br>
User akan disuruh memasukan nama dan jumlah hutang.<br><br>
*a). Kalau benar (misalnya Bastian, 1000000):* <br>
<img width="404" height="117" alt="image" src="https://github.com/user-attachments/assets/e27e6b97-7bc0-4fc6-8aa6-4e3d9fe9a051" /> <br><br>

*b). Kalau jumlah bukan angka bulat (misalnya huruf, simbol, dll):* <br>
<img width="492" height="105" alt="image" src="https://github.com/user-attachments/assets/176a2f45-59ea-45db-9e2e-e05efa0ba251" /> <br><br>

**2. Lihat Hutang**<br>
<img width="402" height="257" alt="image" src="https://github.com/user-attachments/assets/ed0ba292-3916-49d9-8c86-7db9e290f104" /> <br>
Saat memilih Lihat Hutang, maka akan ditunjukan daftar hutang yang ada, dan juga hutang yang baru dibuat. <br><br>
**3. Ubah Hutang** <br>
<img width="396" height="226" alt="image" src="https://github.com/user-attachments/assets/3930018b-bc4d-4908-b7c7-2d1a17132f62" /> <br>
pertama-tama akan menunjukan daftar hutang yang ada. <br><br>

<img width="469" height="251" alt="image" src="https://github.com/user-attachments/assets/6357cd14-da1a-4e32-bd6c-de19c0571884" /> <br>
Lalu disuruh masukan ID yang mau diubah<br><br>
*a). Kalau ID benar, lanjut* <br>
<img width="415" height="277" alt="image" src="https://github.com/user-attachments/assets/5776efd0-647a-4d6a-97a4-698f1ce8405a" /> <br><br>

*b). Kalau valid* <br>
<img width="388" height="337" alt="image" src="https://github.com/user-attachments/assets/01a2be9b-e364-48d0-a547-6efa585b915d" /> <br><br>


*c). Kalau salah input (bukan angka)* <br>
<img width="458" height="341" alt="image" src="https://github.com/user-attachments/assets/2ee835be-9311-4190-ae5f-51cd92f8cff9" /> <br><br>

*d). kalau ID tidak ada:* <br>
<img width="419" height="53" alt="image" src="https://github.com/user-attachments/assets/b286615f-9a67-4884-8f75-10d2322bc012" /> <br><br>

**4. Hapus Hutang (hanya Manager)** <br>
Tampillkan tabel, lalu:. <br>
<img width="411" height="260" alt="image" src="https://github.com/user-attachments/assets/6c1ac765-63a3-4048-8e68-6e9368d275bc" /> <br><br>

*a). Kalau ID benar:* <br>
<img width="390" height="287" alt="image" src="https://github.com/user-attachments/assets/fa84837a-af06-4db3-91b2-76157fad8aeb" /> <br><br>

*b). Kalau ID salah:* <br>
<img width="391" height="284" alt="image" src="https://github.com/user-attachments/assets/13e82670-5125-498c-a81d-e5118904e4a9" /> <br><br>

*c). Kalau input bukan angka:* <br>
<img width="407" height="289" alt="image" src="https://github.com/user-attachments/assets/d7b4efca-0920-4658-aea2-a7c837cc73bf" /> <br><br>

**5. Keluar Program (Manager) atau 4 / 2 (Karyawan/Viewer)** <br>
<img width="232" height="26" alt="image" src="https://github.com/user-attachments/assets/b089ff90-80ac-47c7-8e8d-07e8a719d5cc" /> <br>
program berhenti. <br><br>

**6. Kalau pilih menu yang tidak ada** <br>
<img width="292" height="52" alt="image" src="https://github.com/user-attachments/assets/b5a658f3-ef82-40bc-8677-2152c3720e5b" /> <br><br>

**Sekian Penjelesan terkait program yang telah di update, Terima Kasih**













