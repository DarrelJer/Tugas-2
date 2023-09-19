# Tugas-2
#Darrel Jeremiah Simanjuntak, 2206829225, KA, PBP B

#Tautan
Tautan menuju adaptable : https://proyek-pbp-sepuh.adaptable.app

#Pengerjaan Checklist
- Pertama-tama saya membuat direktori baru pada laptop saya kemudian saya mengaktifkan virtual enviroment.
- Selanjutnya pada direktori tersebut saya membuat dependencies dalam requirements.txt dan memasang dependencies tersebut.
- Setelah saya melakukan kedua hal di atas, saya menyambungkan direktori saya ke repositori github saya.
- Kemudian saya membuat project Django baru pada direktori yang telah saya tentukan.
- Selanjutnya, saya melakukan konfigurasi pada settings.py dengan memberikan akses pada host dengan menambahkan "*" dan saya mencoba untuk menjalankan server Django yang telah saya buat.
- Berikutnya, saya membuat aplikasi main pada direktori saya dengan menjalankan kode python3 manage.py startapp main
- Setelah membuat aplikasi main, saya menambahkan aplikasi tersebut pada settings.py di direktori proyek supaya aplikasi terdaftar pada proyek tersebut.
- Kemudian saya membuat model pada aplikasi dengan memodifikasi berkas models.py sesuai ketentuan soal dengan membuat atribut name, ammount, dan description dengan tipenya masing-masing.
- Setelah membuat model, saya melakukan mingrasi model untuk menyimpan model dan atributnya dalam database.
- Selanjutnya, saya membuat function show_main pada berkas views.py untuk menghubungkan views dengan template HTML, function show_main menerima parameter request yang akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
- Kemudian saya membuat urls.py pada direktori aplikasi main untuk memetakan function pada views.py, dalam urls.py terdapat function path yang menerima parameter ' ' agar halaman aplikasi tersebut muncul pada halaman utama localpath.
- Setelah mengkonfigurasi routing URL aplikasi, saya melakukan konfigurasi pada URL proyek untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
- Selanjutnya saya menjalankan proyek Django dengan perintah python3 manage.py runserver
- Terakhir, untuk mendeploy ke Adaptable, saya mengikuti langkah-langkah pada tutorial 0.


**Bagan**

![image](https://github.com/DarrelJer/Tugas-2/assets/124592793/ceaa00b1-3e3c-4ab3-a4a6-c55843c1fcd9)






**Penjelasan mengapa menggunakan virtual enviroment**
Kita menggunakan virtual environment pada penggunaan Django dikarenakan memiliki manfaat seperti :

- Stable Environments Dengan menggunakan virtual environments, kita mengisolasikan project yang kita buat dari sistem yang lain. Ini berarti perubahan yang terjadi pada sistem atau proyek yang lain tidak akan mengganggu stabilitas dari proyek yang sedang kita buat.
- Reproducible Enviroments Virtual environment menyediakan kita fasilitas untuk membuat enviroment yang dapat dibuat ulang dengan memberikan detail versi Python dan packages lain yang diperlukan dari proyek yang sedang kita buat.
  
Penggunaan virtual enviroment tidak diwajibkan, tetapi ini adalah praktik terbaik untuk menghindari masalah dengan memastikan kebersihan, isolasi, dan manajemen dependensi yang efisien.

**Penjelasan MVT, MVC, MVVM, dan perbedaannya**

- MVC (Model - View - Controller):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    Controller: Menentukan tampilan antarmuka pengguna.
- MVT (Model - View - Template):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    Template: Mengatur tampilan HTML dan cara data dari Model ditampilkan dalam halaman web.
- Model-View-ViewModel (MVVM):
    Model: Menyimpan data dan logika aplikasi.
    View: Menampilkan data dari model dan menghubungkannya dengan template.
    ViewModel: Memproses data dari Model dan mempersiapkannya untuk ditampilkan oleh View.

Perbedaan :
- MVC memisahkan tugas menjadi Model, View, dan Controller dengan Controller sebagai pengendali interaksi.
- MVT mirip dengan MVC, tetapi menggunakan Template sebagai bagian terpisah yang mengontrol tampilan.
- MVVM memisahkan tugas menjadi Model, View, dan ViewModel dengan ViewModel bertindak sebagai perantara yang mengelola tampilan dan interaksi pengguna.


    
