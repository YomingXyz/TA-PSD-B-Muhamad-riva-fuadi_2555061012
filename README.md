A. PROGRAM MANAJEMEN STOK BARANG DENGAN INSERTION SORT

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk manajemen inventaris atau stok barang. Pengguna dapat menambahkan data barang baru (nama dan jumlah stoknya), melihat daftar stok barang yang sudah diinputkan secara mentah (belum terurut), serta mengurutkan daftar barang tersebut dari jumlah stok paling sedikit ke paling banyak menggunakan algoritma Insertion Sort. Program berjalan dalam loop hingga pengguna memilih untuk keluar dari program. Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data jumlah stok dan pilihan menu yang dimasukkan berupa angka yang valid agar tidak menimbulkan error. Struktur data yang digunakan dalam program ini adalah List 2 Dimensi, di mana list utama data_stok menyimpan sekumpulan elemen list yang masing-masing berisi pasangan [nama_barang, jumlah_stok]. Operasi yang dilakukan meliputi penambahan data menggunakan metode append, pengurutan data dengan logika pertukaran elemen berdasarkan indeks (Insertion Sort), serta penelusuran data menggunakan perulangan for berdasarkan panjang list untuk menampilkan output ke layar.

C. Source Code Penjelasan kode per baris:
<img width="792" height="608" alt="Cuplikan layar 2026-05-03 153610" src="https://github.com/user-attachments/assets/647791a0-ec52-4946-bd15-abbb65f46c72" />
<img width="1063" height="600" alt="Cuplikan layar 2026-05-03 153622" src="https://github.com/user-attachments/assets/9369ecd0-354d-4c2c-a8c6-da94e0e30224" />
<img width="1049" height="589" alt="Cuplikan layar 2026-05-03 153632" src="https://github.com/user-attachments/assets/c0f8000a-4d67-488f-a376-28f7708077c0" />
<img width="392" height="73" alt="Cuplikan layar 2026-05-03 153637" src="https://github.com/user-attachments/assets/9e527b43-5ea9-46f3-87a1-683658d930ac" />

1.judul program (komentar)

2.membuat fungsi insertion_sort(arr, n) dengan parameter array dan panjang array

3.perulangan for dengan variabel i mulai dari indeks 1 hingga n-1

4.menyimpan elemen list array indeks ke-i ke dalam variabel temp

5.membuat variabel j yang bernilai i - 1

6.perulangan while selama kondisi j >= 0 dan nilai jumlah elemen ke-j (indeks 1) lebih besar dari nilai jumlah pada variabel temp

7.menggeser posisi elemen indeks ke-j ke kanan (ke posisi j + 1)

8.mengurangi nilai variabel j sebesar 1

9.menempatkan list temp pada posisi akhir penggeseran (indeks j + 1)

10.membuat fungsi main() sebagai program utama

11.membuat list variabel data_stok = [] yang masih berupa list kosong

12.membuat variabel pilih = 0 untuk menyimpan pilihan menu

13.perulangan while yang membuat program terus berjalan selama variabel pilih tidak sama dengan 4

14.mencetak judul menu program

15.mencetak menu pertama untuk tambah stok barang

16.mencetak menu kedua untuk menampilkan stok belum terurut

17.mencetak menu ketiga untuk mengurutkan dengan Insertion Sort dan menampilkannya

18.mencetak menu keempat untuk keluar dari program

19.program akan mencoba

20.meminta user untuk input pilihan menu yang dikonversi ke integer

21.pengecualian jika value yang diinputkan error (bukan angka)

22.program akan mencetak peringatan masukkan angka yang valid

23.continue berfungsi untuk membuat program kembali ke looping awal (menampilkan menu)

24.pengondisian jika user memilih menu 1

25.meminta user untuk input nama barang dan menyimpannya di variabel nama

26.program akan mencoba

27.meminta user input jumlah stok dan menyimpannya di variabel jumlah dengan tipe data integer

28.nilai variabel nama dan jumlah dimasukkan ke dalam list data_stok sebagai list 2 dimensi menggunakan operasi append

29.mencetak pesan berhasil memasukkan barang beserta nama dan jumlahnya

30.pengecualian jika input jumlah error (bukan angka)

31.program akan mencetak peringatan untuk memasukkan angka

32.pengondisian jika user memilih menu 2

33.pengondisian jika panjang list data_stok sama dengan 0

34.program mencetak "(kosong)"

35.else, kondisi jika list sudah terisi

36.mencetak tulisan "Daftar Stok Saat Ini:"

37.perulangan for untuk melakukan iterasi sepanjang jumlah elemen di data_stok

38.mencetak nama barang dan jumlahnya memanggil elemen dari list 2 dimensi

39.pengondisian jika user memilih menu 3

40.membuat variabel n yang menyimpan nilai panjang dari list data_stok

41.pengondisian jika n sama dengan 0

42.program mencetak "(kosong)"

43.else, kondisi jika list terisi

44.memanggil fungsi insertion_sort(data_stok, n) untuk mengurutkan data

45.mencetak judul daftar stok setelah diurutkan dari terkecil ke terbesar

46.perulangan for iterasi sebanyak nilai n

47.mencetak nama barang dan jumlah stok yang posisinya sudah terurut di dalam list

48.pengondisian jika user memilih menu 4

49.mencetak "Program selesai."

50.kondisi jika user menginputkan selain angka 1, 2, 3 dan 4

51.program mencetak "Pilihan tidak valid!"

52.entry point, pengecekan if __name__ == "__main__": agar program hanya berjalan saat dieksekusi langsung

53.memanggil fungsi main() untuk menjalankan program

D. Output Program
<img width="664" height="1040" alt="Cuplikan layar 2026-05-03 195552" src="https://github.com/user-attachments/assets/b31b9b80-f268-47c5-b84f-68b696fa3784" />
<img width="667" height="652" alt="Cuplikan layar 2026-05-03 195602" src="https://github.com/user-attachments/assets/6f237202-011e-48e2-9a55-695c8545cc60" />
Penjelasan Output: Program akan langsung menampilkan menu saat dijalankan dan meminta user untuk menginputkan pilihan menu. Saat user memilih menu 1, program meminta user untuk menginputkan nama barang. User menginputkan "Beras", lalu program meminta jumlah stok, user menginputkan angka 50. Program mencetak pesan bahwa "Beras" dengan jumlah 50 berhasil dimasukkan. Program mengulang dan menampilkan menu kembali. User memilih menu 1 lagi, menginputkan "Minyak Goreng" dengan jumlah 15. User kembali memilih menu 1, menginputkan "Gula Pasir" dengan jumlah 30. Tahap selanjutnya, user memilih menu 2. Program akan menampilkan teks "Daftar Stok Saat Ini:" dilanjutkan daftar barang secara urut sesuai waktu input (Beras : 50, Minyak Goreng : 15, Gula Pasir : 30). Kemudian, program kembali ke menu dan user memilih menu 3. Program menjalankan algoritma Insertion Sort di belakang layar, lalu menampilkan teks "Daftar Stok Setelah Diurutkan (Terkecil - Terbesar):" beserta daftarnya yang kini posisinya sudah berubah terurut berdasarkan jumlah (Minyak Goreng : 15, Gula Pasir : 30, Beras : 50). Selanjutnya, user menginputkan menu 4 untuk keluar, program mencetak pesan "Program selesai.", dan perulangan pun berakhir.

Link Youtube:
