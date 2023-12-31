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


    


# Tugas 3

**1. Perbedaan POST dan GET dalam Django**
     Dalam Django, `POST` dan `GET` umumnya digunakan untuk tujuan yang berbeda.
     `POST` digunakan dalam pengisian form Django dimana *browser* akan menggabungkan data form, mengenkode untuk pengiriman, mengirimkan datanya ke server, dan menerima responsnya.
   `GET` sebaliknya, dimana `GET` akan menggabungkan data yang dikirim ke dalam string dan menggunakannya untuk menyusun URL. URL tersebut berisi alamat tempat data harus dikirimkan, serta _keys_ dan _value_ dari data tersebut.


**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**
- XML : XML adalah bahasa markup yang menggunakan tag untuk mendefinisikan struktur dan makna data. XML dapat digunakan untuk menyimpan data yang kompleks. XML memisahkan data dari HTML dan menyederhanakan proses perubahan platform.
- JSON : JSON adalah format data ringan yang digunakan untuk pertukaran data di web. JSON lebih sering digunakan untuk mengirim data dari server ke peramban web dan sebaliknya. JSON menggunakan pasangan key-values untuk merepresentasikan data.
- HTML : HTML adalah bahasa markup yang digunakan untuk membuat halaman web dan aplikasi web. HTML menggunakan tag untuk menentukan struktur dan penampilan data. HTML dirancang untuk menampilkan data, bukan untuk mengangkut data. HTML tidak dapat menyimpan data yang kompleks atau terstruktur seperti XML atau JSON.


**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
JSON lebih sering digunakan karena JSON dirancang _self-decsribing_ yang membuat JSON lebih mudah untuk dibaca dan dipahami, JSON juga memiliki file yang lebih ringan yang membuat JSON lebih cepat dan efisien dalam mengirim dan menerima data melalui jaringan. JSON juga dapat menyimpan data yang ringan dan terstruktur, seperti objek, array, atau nilai primitif. Hal ini cocok untuk aplikasi web modern yang membutuhkan data yang dinamis dan interaktif.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**

**Membuat `base.html` sebagai template untuk template-template HTML lainnya.**
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

**Mengedit `TEMPLATES` yang ada pada `settings.py` agar `base.html` bisa terdeteksi sebagai file template.**
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```

**Mengubah kode pada berkas `main.html` agar menggunakan `base.html` sebagai template utamanya.**
```
{% extends 'base.html' %}
...
```

**Membuat `forms.py` untuk membuat struktur form dan meng-import form tersebut pada `views.py`.**
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

**Membuat function `create_product` pada `views.py` agar formulir yang dibuat  dapat menambahkan data produk secara otomatis ketika data di-submit dari form.**

```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

**Mengubah fungsi `show_main` pada `views.py` supaya data dapat diakses pada `main.html`**
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Darrel Jeremiah',
        'class': 'PBP B',
        'products': products
    }

    return render(request, "main.html", context)
```

```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

**Membuat fungsi `show_json` dan `show_xml` pada `views.py` dan menambahkannya pada `urls.py`**
- Membuat function `show_json`
    ```
    def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
- Function `show_xml`

  ```
    def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
  ```
- Meng-import kedua function tersebut pada `urls.py`
  ```
  from main.views import show_main, create_product, show_xml, show_json
  ```

- Membuat url untuk kedua fungsi tersebut agar dapat diakses sesuai url-nya masing-masing
  ```
  ...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    ...
  ```


**Membuat fungsi  `show_xml_by_id` dan `show_json_by_id` pada `views.py` dan menambahkannya pada `urls.py`**

- `show_xml_by_id`
    ```
    def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
- `show_json_by_id`
  ```

  def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```
- Meng-import kedua fungsi tersebut pada `urls.py`
    ```
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
- Membuat url untuk kedua fungsi tersebut agar dapat diakses sesuai url-nya masing-masing
  ```
  ...
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
  ...
  ```

**5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
- JSON
    <img width="1392" alt="image" src="https://github.com/DarrelJer/Tugas-2/assets/124592793/c2ae163c-1c9e-4a41-8a42-eeafb9ef378e">

- XML
    <img width="1392" alt="image" src="https://github.com/DarrelJer/Tugas-2/assets/124592793/2690e91d-dff9-4e5b-a3db-f6876d4370e3">

- HTML
    <img width="1392" alt="image" src="https://github.com/DarrelJer/Tugas-2/assets/124592793/9df14e3e-a668-4053-93c3-0d164f3f2a14">

- JSON by ID
    <img width="1392" alt="image" src="https://github.com/DarrelJer/Tugas-2/assets/124592793/ad41f2ee-101d-494b-9bbd-f8aadb47b0dd">
- XML by ID
    <img width="1392" alt="image" src="https://github.com/DarrelJer/Tugas-2/assets/124592793/a70607a0-24be-42ca-9d72-521ddf1d3fbd">



# Tugas 4

**1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
  Django UserCreationForm adalah sebuah form yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web kita. Form ini memiliki tiga bidang yaitu:        username, password1, dan password2.  
  
  Kelebihan : 
    - Mudah digunakan dan dapat dimodifikasi dengan mudah.
    - Secara _default_ form ini sudah menyediakan bidang verifikasi, sehingga kita tidak perlu            menuliskannya lagi.

  Kelemahan : 
    - Form ini cocok untuk skenario autentikasi sederhana, jika kita mau menggunakan autentikasi dengan metode lain (seperti dengan nomor gawai atau melalui email), maka kita perlu membuat form sendiri atau dengan _third parties_
  
**2.Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

- Autentikasi : Proses verifikasi identitas pengguna. Pada implementasinya biasanya menggunakan form untuk login.
- Otorisasi : pengendalian hak akses pengguna setelah pengguna tersebut berhasil diautentikasi

  Keduanya penting untuk memproteksi dan menjamin keamanan data milik seseorang dan fitur ini berguna untuk mengatur fungsi dari website dengan memberikan fasilitas-fasilitas.

**3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

  Cookies adalah sejenis data yang disimpan di komputer atau perangkat pengguna saat mereka berinteraksi pada web. Cookies digunakan untuk berbagai tujuan, termasuk pengelolaan sesi pengguna, pelacakan perilaku pengguna, dan penyimpanan preferensi pengguna. Salah satu penggunaan utama cookies adalah untuk mengidentifikasi pengguna dan menyimpan informasi tertentu tentang mereka selama kunjungan mereka ke sebuah situs web.

  Dalam konteks Django, cookies sering digunakan untuk mengelola data sesi pengguna. Sesuai dengan pendekatan stateless HTTP, di mana setiap permintaan dari browser dianggap independen, Django menggunakan cookies untuk mengidentifikasi dan melacak sesi pengguna.

**4.Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

  Penggunaan cookies dalam web bersifat aman jika digunakan dengan benar, risiko potensial yang harus diwaspadai adalah:
  - Data Senditif : Cookies dapat digunakan untuk menyimpan data sensitif seperti token otentikasi atau informasi pengguna.
  - Cross-Site Scripting : Cross Site Scripting adalah jenis serangan yang dapat mengakibatkan skrip berbahaya dijalankan pada browser pengguna.
  - CSRF :  Serangan CSRF melibatkan penggunaan cookies untuk mengirim permintaan palsu yang tampaknya berasal dari pengguna yang sah.
  - _Data Exposure_ : Jika cookies tidak diatur dengan benar, informasi sensitif seperti nama pengguna atau ID pengguna dapat terungkap jika peretas berhasil mencurinya



# Tugas 5
**1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
- Element Selector: Element selector akan memberikan kita akses untuk mengubah properti elemen yang memiliki tag yang sama. Selector ini digunakan saat kita ingin mengganti atribut semua elemen tertentu pada suatu berkas HTML.
- ID Selector : ID yang unik dalam satu halaman web akan digunakan sebagai selectornya. Selector ini digunakan saat kita ingin mengganti sebuah element yang memiliki ID tersebut saja.
- Class Selector : Class selector memberikan kita akses untuk mengubah properti dengan mengelompokkan elemen yang memiliki karakteristik serupa. Selector ini digunakan saat kita ingin mengganti style dari suatu bagian program yang sama atau memiliki fungsi yang sama.
  

**2. Jelaskan HTML5 Tag yang kamu ketahui.**
- ```<h1>```, ```<h2>```, ```<h3>```, ```<h4>```, ```<h5>```, dan ```<h6>``` adalah heading yang dapat digunakan sebagai judul atau subjudul
- ```<p>``` untuk mendefinisikan paragraf teks
- ```<table>``` untuk membuat table untuk mengorganisir data
- ```<tr>```, ```<th>```, ```<td>``` digunakan di dalam table untuk mendefinisikan rows, header, dan data
- ```<div>```  digunakan untuk mendefinisikan container umum yang akan digunakan untuk mengelompokkan dan membuat struktur dari konten yang dibuat

Itu adalah beberapa tag yang saya ketahui dan umum digunakan dalam tugas-tugas PBP.

**3. Jelaskan perbedaan antara margin dan padding.**
- Margin : Memberikan ruang atau spacing kosong di luar border (Bagian paling luar)
- Padding : Memberikan ruang atau spacing kosong di luar content (Antara border dan content)

Margin dan padding sama-sama mengosongkan ruang, tetapi margin berada di **bagian luar border** sedangkan padding berada **di antara border dan content**.

**4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
1) Ukuran File
     - Bootstrap: Karena Bootstrap sudah menyediakan banyak komponen dan desain, file CSS dan JavaScript yang ada berukuran cukup besar dan dapat mempengaruhi kinerja situs web kita. 
     - Tailwind: Tailwind CSS memiliki file CSS yang lebih kecil karena hanya menghasilkan kelas yang Anda gunakan. Ini dapat mengurangi ukuran file dan mempercepat waktu pemuatan situs Anda.

2) Kemudahan Penggunaan
     - Boostrap: Bootstrap memiliki komponen dan tata letak yang sudah didefinisikan, sehingga cocok untuk proyek yang membutuhkan pengembangan cepat tanpa banyak kustomisasi.Hal ini sangat berguna untuk pemula atau untuk orang yang ingin membangun prototipe dengan cepat.
     - Tailwind: Tailwind lebih cocok untuk proyek-proyek di mana kita ingin merancang tampilan dengan sangat detail atau memiliki kebutuhan desain yang unik. Ini memerlukan lebih banyak penulisan kode tetapi memberikan kendali yang lebih besar.

3) Kustomisasi
     - Bootstrap menyediakan sejumlah opsi untuk mengkustomisasi , tetapi umumnya kita perlu menambahkan CSS tambahan atau memanipulasi gaya bawaan Bootstrap untuk mencapai tampilan yang diinginkan.
     - Tailwind : Tailwind dirancang untuk kustomisasi yang lebih _expert_ atau detil. Kita dapat dengan mudah menyesuaikan tampilan Anda dengan menambahkan atau mengubah kelas CSS sesuai kebutuhan kita.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
  Saya mengubah tampilan halaman Login dengan mengubah login.html seperti berikut
  ```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">
    <div class = "container text-center">
        <div class = "row">
            <h1 class="login-head">INI BUKAN TOKO BANGUNAN!!!</h1>
            <h2 class="login-msg">Silahkan Login.</h2>
        </div>
        <div class = "row justify-content-center align-items-center">
            <form method="POST" action="">
                {% csrf_token %}
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        vertical-align: middle;
                    }
                    
                    th, td {
                        text-align: center;
                        vertical-align: middle;
                        padding: 10px; 
                    }
                </style>
                <table>
                    <tr>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr></tr>
                        <td><input class="btn btn-primary login_btn" type="submit" value="Login" style = "background-color: #252525; border:transparent"></td>
                    </tr>
                </table>
            </form> 
                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}     
                Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        </div>
    </div>
</div>

{% endblock content %}
```

# Tugas 6

**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
- Asynchronous:Operasi dieksekusi secara independen tanpa harus menunggu yang lain, Waktu respon lebih cepat, Penggunaan callback atau await/async untuk mengelola operasi asynchronous, dan Cocok untuk operasi jaringan, I/O berat, dan aplikasi yang perlu responsif terhadap input
- Synchcronous : Operasi dieksekusi berurutan, satu per satu, Waktu respons lebih lambat karena operasi harus menunggu operasi sebelumnya selesai, Tidak memerlukan pengaturan khusus seperti callback, Cocok untuk tugas-tugas sederhana dan cepat

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-driven programming digunakan untuk membangun aplikasi web yang responsif dan interaktif. Dalam tugas ini, paradigma ini terlihat pada tombol yang memicu fungsi addItem() dan deleteItem() ketika tombol "Add Item" atau "Delete" ditekan.

**3. Jelaskan penerapan asynchronous programming pada AJAX.**
Asynchronous programming pada AJAX adalah cara untuk melakukan operasi seperti pengambilan data dari server tanpa menghentikan eksekusi kode utama. Hal ini membuat aplikasi web tetap responsif dan efisien.

**4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**
- Fetch API: Fetch API menyediakan Interface untuk mengambil resource. Fetch API memungkinkan untuk mengirim permintaan HTTP secara asynchronous dengan lebih efisien.
- jQuery : jQuery adalah library JavaScript yang lebih besar dengan banyak fitur, termasuk fitur untuk mengirim permintaan HTTP asynchronous.
Menurut saya, Fetch API lebih baik digunakan karena keunggulannya yang memiliki performa yang lebih optimal dan responsif dibandingkan dengan jQuery.




