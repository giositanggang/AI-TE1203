#Implementasi Search Algorithm dan Expert System Menggunakan Python

##1. Introduction

Proyek ini dibuat untuk memenuhi tugas mata kuliah Kecerdasan Buatan (Artificial Intelligence). Program ini mengimplementasikan dua konsep dasar dalam kecerdasan buatan, yaitu Search Algorithm dan Expert System, menggunakan bahasa pemrograman Python.

Search Algorithm digunakan untuk mencari jalur dari titik awal menuju titik tujuan menggunakan algoritma Breadth-First Search (BFS). Sementara itu, Expert System digunakan untuk membantu melakukan pemeriksaan awal terhadap kondisi komputer berdasarkan jawaban yang diberikan oleh pengguna.

##2. Objectives

Tujuan dari proyek ini adalah:

Memahami penerapan algoritma pencarian dalam kecerdasan buatan.

Mengimplementasikan algoritma Breadth-First Search (BFS) untuk menemukan jalur pada sebuah graf.

Mengimplementasikan sistem pakar sederhana berbasis aturan untuk pemeriksaan awal komputer.

Memahami penggunaan input, percabangan, fungsi, dan struktur data dalam Python.

##3. Programs

A. Search Algorithm — Breadth-First Search (BFS)

Program Search Algorithm menggunakan algoritma BFS untuk mencari jalur antara dua titik pada graf yang merepresentasikan hubungan antar lokasi.

Fitur:

Menampilkan daftar titik yang tersedia.

Menerima input titik awal dan titik tujuan.

Memvalidasi titik yang dimasukkan pengguna.

Mencari jalur menggunakan algoritma BFS.

Menampilkan jalur yang ditemukan dan jumlah langkah.

Contoh penggunaan:

Input:

Titik awal: A

Titik tujuan: G

Output:

Jalur ditemukan: A -> C -> F -> G
Jumlah langkah: 3

B. Expert System — Pemeriksaan Awal Komputer

Program Expert System merupakan sistem pakar sederhana yang memberikan rekomendasi pemeriksaan awal komputer berdasarkan gejala yang dilaporkan pengguna.

Fitur:

Memeriksa apakah komputer menyala.

Memeriksa apakah layar menampilkan gambar.

Memeriksa apakah komputer terasa lambat.

Memberikan rekomendasi berdasarkan jawaban pengguna.

Memvalidasi input agar sesuai dengan pilihan yang tersedia.

Sistem menggunakan aturan berbasis kondisi (rule-based system) untuk menentukan rekomendasi yang sesuai.

##4. Technologies Used

Programming Language: Python

Code Editor: Visual Studio Code

Search Algorithm: Breadth-First Search (BFS)

Data Structure: Dictionary, List, Set, dan Queue (deque)

##5. Project Structure

AI-TE1203-main/
├── expert_system.py
├── main.py
├── README.md
└── search_algorithm.py

Keterangan:

expert_system.py: Program sistem pakar pemeriksaan awal komputer.

search_algorithm.py: Program pencarian jalur menggunakan BFS.

main.py: File program utama atau file pendukung proyek, sesuai isi kode yang digunakan.

README.md: Dokumentasi proyek.

##6. Requirements

Untuk menjalankan program, diperlukan:

Python 3.

Visual Studio Code atau editor Python lainnya.

Terminal untuk menjalankan program.

##7. How to Run the Programs

Pastikan Python telah terpasang pada komputer dan terminal sudah berada di folder proyek.

A. Menjalankan Search Algorithm

Jalankan perintah berikut pada terminal:

python search_algorithm.py

Masukkan titik awal dan titik tujuan sesuai instruksi program.

B. Menjalankan Expert System

Jalankan perintah berikut:

python expert_system.py

Jawab pertanyaan mengenai kondisi komputer dengan memasukkan ya atau tidak.

##8. Testing

Pengujian dilakukan dengan memasukkan beberapa kombinasi input untuk memastikan program berjalan sesuai aturan yang telah dibuat.

Search Algorithm:

Menguji pencarian jalur dari A menuju G.

Menguji input titik yang tidak tersedia.

Menguji pencarian dari titik awal ke tujuan yang sama.

Expert System:

Menguji kondisi komputer tidak menyala.

Menguji kondisi layar tidak menampilkan gambar.

Menguji kondisi komputer terasa lambat.

Menguji kondisi tidak ditemukan gejala utama.

Menguji input yang tidak valid.

Hasil pengujian dicatat berdasarkan keluaran yang ditampilkan saat program dijalankan.

##9. Conclusion

Proyek ini menunjukkan penerapan dua konsep kecerdasan buatan menggunakan Python. Algoritma BFS dapat digunakan untuk mencari jalur dengan jumlah langkah minimum pada graf yang tidak berbobot, sedangkan Expert System dapat memberikan rekomendasi pemeriksaan awal komputer berdasarkan aturan dan jawaban pengguna.

Melalui proyek ini, mahasiswa dapat memahami konsep dasar pencarian, penalaran berbasis aturan, dan implementasi sederhana kecerdasan buatan dalam pemrograman.

##10. Team Members

Manager: Giovani Yulianto

Developer 1: Yales Nof Romy T Mendrofa

##11. Repository

Repository ini dibuat sebagai bagian dari tugas mata kuliah Kecerdasan Buatan (Artificial Intelligence).
