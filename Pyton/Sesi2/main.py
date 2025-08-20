#library
import random

welcomeMessage = "CUYPY GAMES!" 
cuypy_position = random.randint(1, 4)

print("******************")
print(f"** {welcomeMessage} **")
print("******************")
    
bentuk_goa = "|_|"
goa = [bentuk_goa] * 4

# buat salinan goa untuk menampilkan goa kosong
goa_kosong = goa.copy()

# isi goa_cuypy di dalam goa
goa[cuypy_position - 1] = "|0_^|"


nama_user = input("Masukkan nama kamu: ")

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini 
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
#input itu string, jadi harus diubah ke int jika ingin dibandingkan dengan angka

print (f"pilihan kamu adalah {pilihan_user}")
print()
konfirmasi_jawaban = input("Apa kamu yakin dengan pilihanmu?[y/n]: ")

if konfirmasi_jawaban.lower() == 'n':
    print("oh ga yakin yah? keluar sistem...")
    exit()
elif konfirmasi_jawaban.lower() == 'y':
    print("Kamu yakin dengan pilihanmu!")
    if pilihan_user == cuypy_position:
        print(f"Selamat {nama_user}, kamu berhasil. {goa}")
    else:
        print(f"Yahh {nama_user}... kamu salah nihh. {goa}")
else:
    print("Pilihan tidak valid. Program akan keluar.")
    exit()
    
    


