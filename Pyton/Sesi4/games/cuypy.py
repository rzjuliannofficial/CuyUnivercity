import random
import socket 
import main

nama_user = socket.gethostname()

def start():
    while True:
        cuypy_position = random.randint(1, 4)
        bentuk_goa = "|_|"
        goa = [bentuk_goa] * 4
        goa_kosong = goa.copy()
        goa[cuypy_position - 1] = "|0_^|"
        goa_kosong = '-'.join(goa_kosong)
        goa = '-'.join(goa)
        
        print(f'Halo {nama_user}! Coba perhatikan goa dibawah ini \n\n{goa_kosong}\n')

        pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))
        #input itu string, jadi harus diubah ke int jika ingin dibandingkan dengan angka

        print (f"pilihan kamu adalah {pilihan_user}")
        print()

        if pilihan_user == cuypy_position:
            print(f"\nSelamat {nama_user}, kamu berhasil.")
            print(f"\n{goa}")
        else:
            print(f"\nYahh {nama_user}... kamu salah nihh.")
            print(f"\n{goa}")
            
        play_again = input("\nMau main lagi? [y/n]: ")
        if play_again.lower() == 'n':
            main.menu()


if __name__ == "__main__":
    start()
