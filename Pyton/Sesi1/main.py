#library
import random

welcomeMessage = "CUYPY GAMES!" 
cuypy_position = random.randint(1, 4)

print("******************")
print(f"** {welcomeMessage} **")
print("******************")

# nomor_Saya = 0

# if nomor_Saya == 4:
#     print("Nomor saya adalah 4")
# else:
#     print("ah bukan 4 ternyata...")
    
nama_user = input("Masukkan nama kamu: ")
print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini 
|_| |_| |_| |_| 
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
#input itu string, jadi harus diubah ke int jika ingin dibandingkan dengan angka

print (f"pilihan kamu adalah {pilihan_user}")
print()
validasi_user = input("Apa kamu yakin dengan pilihanmu? [y/n]: ")

if validasi_user.lower() == 'y':
    print("Kamu yakin dengan pilihanmu!")
    if pilihan_user == cuypy_position:
        print(f"Selamat {nama_user}, kamu berhasil menemukan CUYPY di goa nomor {cuypy_position}!")
    elif pilihan_user != cuypy_position:
        print(f"Yahh {nama_user}... kamu salah nihh. CUYPY gada di goa nomor {pilihan_user}")
else:
    print("oh ga yakin yah? yaudah lah")
    
    


