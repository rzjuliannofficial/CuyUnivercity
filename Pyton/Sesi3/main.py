#library
import random
from libs import welcome_message

cuypy_position = random.randint(1, 4)

welcome_message("WELCOME TO CUYPY GAME")

#Sesi 3
# for i in range(5).__reversed__():
#     # print(f"** GOA {i} **")    

# i = 0
# while i < 4:
#     # print(f"** GOA {i} **")
#     i += 1

bentuk_goa = "|_|"
goa = [bentuk_goa] * 4

# buat salinan goa untuk menampilkan goa kosong
goa_kosong = goa.copy()

# isi goa_cuypy di dalam goa
goa[cuypy_position - 1] = "|0_^|"

#SESI3
# mengubah goa_kosong menjadi string untuk ditampilkan
# dengan cara menjoin array menjadi string
goa_kosong = '-'.join(goa_kosong)
goa = '-'.join(goa)


nama_user = input("Masukkan nama kamu: ")

while nama_user == "":
    nama_user = input("Masukkan dulu nama kamu: ")

while True:
    print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini 
{goa_kosong}
''')

    pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
    #input itu string, jadi harus diubah ke int jika ingin dibandingkan dengan angka

    print (f"pilihan kamu adalah {pilihan_user}")
    print()
    konfirmasi_jawaban = input("Apa kamu yakin dengan pilihanmu?[y/n]: ")
    while konfirmasi_jawaban == "":
        konfirmasi_jawaban = input("Kamu harus jawab dulu! [y/n]: ")
        
    if konfirmasi_jawaban.lower() == 'n':
        print("oh ga yakin yah? keluar sistem...")
        exit()
    elif konfirmasi_jawaban.lower() == 'y':
        if pilihan_user == cuypy_position:
            print(f"\nSelamat {nama_user}, kamu berhasil.")
        else:
            print(f"\nYahh {nama_user}... kamu salah nihh.")
            surrend = input("nyerah? [y/n]: ")
            if surrend.lower() == 'y':
                print(f"CUYPY ada di goa nomor {cuypy_position}")
                print(f"\n{goa}")
    else:
        print("Pilihan tidak valid. Program akan keluar.")
        exit()
        
    play_again = input("Mau main lagi? [y/n]:")
    if play_again.lower() == 'n':
        break

print("Terima kasih sudah bermain. Sampai jumpa lagi!")

