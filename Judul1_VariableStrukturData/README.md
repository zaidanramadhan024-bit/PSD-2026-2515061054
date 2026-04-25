Program Catatan Keuangan Sederhana Menggunakan List 1 Dimensi

Program ini merupakan implementasi dari struktur data list 1 dimensi, di mana user dapat mencatat pemasukan dan pengeluaran. User bisa memasukkan jumlah uang yang masuk dan keluar, kemudian program akan menyimpannya ke dalam array yang sudah disediakan.

Jika user menambahkan data, maka data tersebut akan disimpan sesuai urutan index dalam array. Karena menggunakan array dengan ukuran tetap, jumlah data yang bisa dimasukkan dibatasi. Program juga dapat menampilkan seluruh data transaksi serta menghitung total pemasukan, total pengeluaran, dan saldo akhir.
Source Code:

<img width="1032" height="273" alt="Screenshot 2026-04-25 184939" src="https://github.com/user-attachments/assets/b0caab4f-567c-41dc-beac-27200e6dcd51" />

Pada bagian kode pertama, program membuat fungsi menu() yang digunakan untuk menampilkan pilihan menu kepada user. Menu tersebut berisi beberapa fitur seperti menampilkan data transaksi, menambah pemasukan, menambah pengeluaran, menghitung saldo, dan keluar dari program.

<img width="1103" height="308" alt="Screenshot 2026-04-25 185051" src="https://github.com/user-attachments/assets/4230720a-1959-40aa-8968-6a3556a62a6f" />

Pada bagian ini, program membuat dua buah array yaitu pemasukan dan pengeluaran dengan kapasitas masing-masing 5 data. Array ini digunakan untuk menyimpan data yang dimasukkan oleh pengguna.

Selain itu, terdapat juga variabel jumlah_masuk dan jumlah_keluar yang berfungsi untuk menghitung berapa banyak data yang sudah dimasukkan ke dalam masing-masing array. Variabel ini penting karena program menggunakan array dengan ukuran tetap, sehingga perlu penanda untuk mengetahui data mana yang sudah terisi dan mana yang masih kosong.

<img width="1220" height="315" alt="Screenshot 2026-04-25 185934" src="https://github.com/user-attachments/assets/515e17a1-9e9f-4183-be76-d5ef7c3b426b" />

Pada bagian ini, program mulai berjalan menggunakan perulangan while. Selama variabel running bernilai True, program akan terus menampilkan menu dan meminta input dari pengguna.

Untuk menghindari error, input dari pengguna dibungkus dengan try-except. Jadi, jika pengguna salah memasukkan data (misalnya huruf), program tidak akan langsung berhenti, tetapi akan meminta input ulang.

<img width="1322" height="690" alt="Screenshot 2026-04-25 190048" src="https://github.com/user-attachments/assets/54d4bac0-a12e-460f-a5b7-e9730e1dffb9" />

Jika pengguna memilih menu untuk menampilkan data, program akan menampilkan semua pemasukan dan pengeluaran yang sudah dimasukkan.

Program juga akan mengecek apakah data masih kosong. Jika belum ada data, maka akan ditampilkan pesan “Belum ada data”. Jika sudah ada, data akan ditampilkan satu per satu menggunakan perulangan

<img width="1500" height="905" alt="Screenshot 2026-04-25 190305" src="https://github.com/user-attachments/assets/969e567d-a890-47e1-9e1a-897f861f11d8" />

Jika pengguna memilih untuk menambah pemasukan, program akan meminta input berupa jumlah uang, lalu menyimpannya ke dalam array pemasukan.

Data akan dimasukkan sesuai urutan index, dan setelah itu variabel jumlah_masuk akan bertambah satu. Hal yang sama juga berlaku untuk pengeluaran.

Jika data sudah mencapai batas maksimum, program akan menolak input tambahan dan memberi tahu bahwa data sudah penuh.

<img width="1390" height="592" alt="Screenshot 2026-04-25 190356" src="https://github.com/user-attachments/assets/1e9c94cb-bd2e-4c6b-b514-8cd1779b8873" />

Pada bagian ini, program menghitung total pemasukan dan total pengeluaran dengan cara menjumlahkan semua data yang ada di dalam array.

Setelah itu, program menghitung saldo dengan cara mengurangi total pemasukan dengan total pengeluaran. Hasilnya kemudian ditampilkan kepada pengguna.

<img width="1241" height="405" alt="Screenshot 2026-04-25 190431" src="https://github.com/user-attachments/assets/a6272a42-5243-4c5e-a21c-e18d4c88116d" />

Jika pengguna memilih menu keluar, maka program akan berhenti dengan mengubah nilai running menjadi False. Setelah itu, program menampilkan pesan bahwa program telah selesai dijalankan.

Output Program:

Jika pilih menu 1 :

<img width="734" height="374" alt="Screenshot 2026-04-25 190726" src="https://github.com/user-attachments/assets/37bb4d15-818b-4cf3-a111-20eb6dc12c67" />
<img width="813" height="457" alt="Screenshot 2026-04-25 190801" src="https://github.com/user-attachments/assets/a7fe8a18-d62d-4f8d-bbe9-ffafb44f66e8" />


Jika pilih menu 2 :

<img width="839" height="545" alt="Screenshot 2026-04-25 190952" src="https://github.com/user-attachments/assets/94b1e528-240b-42df-a3fb-537f187f9e3f" />


Jika pilih menu 3 :

<img width="907" height="543" alt="Screenshot 2026-04-25 191041" src="https://github.com/user-attachments/assets/1e19d8f1-a4a8-463d-8be6-0399b357d478" />


Jika pilih menu 4 :

<img width="936" height="313" alt="Screenshot 2026-04-25 191129" src="https://github.com/user-attachments/assets/9ed3f963-e19e-4a05-8ff0-c0a67c27297c" />


Jika pilih menu 5 :

<img width="863" height="244" alt="Screenshot 2026-04-25 191219" src="https://github.com/user-attachments/assets/cfb9cfda-eaa8-4f77-882e-071955d59cc3" />

Output Program:

Saat program dijalankan, pengguna akan melihat menu utama yang berisi beberapa pilihan. Pengguna dapat memilih untuk menambahkan pemasukan atau pengeluaran, kemudian data tersebut akan disimpan oleh program.

Setelah beberapa data dimasukkan, pengguna dapat melihat daftar transaksi yang sudah ada. Program akan menampilkan semua pemasukan dan pengeluaran yang telah diinput jika tidak ada data akan menampilkan Belum ada data.

Selanjutnya, pengguna juga bisa melihat hasil perhitungan berupa total pemasukan, total pengeluaran, dan saldo akhir. Dengan begitu, pengguna dapat mengetahui kondisi keuangan secara sederhana.

Jika pengguna memilih keluar, maka program akan berhenti dan menampilkan pesan bahwa program telah selesai.

Link Youtube : https://youtu.be/ZN1T0BIXmcY
