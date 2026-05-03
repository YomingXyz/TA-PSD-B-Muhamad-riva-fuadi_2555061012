def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i] 
        j = i - 1
         
        while j >= 0 and arr[j][1] > temp[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def main():
    data_stok = [] 
    pilih = 0
    
    while pilih != 4:
        print("\n=== PROGRAM MANAJEMEN STOK ===")
        print("1. Tambah Stok Barang")
        print("2. Tampilkan Stok (Belum Terurut)")
        print("3. Urutkan & Tampilkan (Insertion Sort)")
        print("4. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            nama = input("Masukkan nama barang: ")
            try:
                jumlah = int(input("Masukkan jumlah stok: "))
                data_stok.append([nama, jumlah])
                print(f"✅ '{nama}' dengan jumlah {jumlah} berhasil dimasukkan")
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                
        elif pilih == 2:
            if len(data_stok) == 0:
                print("(kosong)")
            else:
                print("Daftar Stok Saat Ini:")
                for i in range(len(data_stok)):
                    print(f"- {data_stok[i][0]} : {data_stok[i][1]}")
                    
        elif pilih == 3:
            n = len(data_stok)
            if n == 0:
                print("(kosong)")
            else:
                insertion_sort(data_stok, n)
                print("Daftar Stok Setelah Diurutkan (Terkecil - Terbesar):")
                for i in range(n):
                    print(f"- {data_stok[i][0]} : {data_stok[i][1]}")
                    
        elif pilih == 4:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
