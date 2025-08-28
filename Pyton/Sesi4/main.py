from libs import welcome_message, exit_program
from games import cuypy
import warung

def menu():
    user_option = int(input('\nmenu program:\n1. Games Cuypy\n2. Warung Mini\n3. Keluar\n\nsilahkan pilih: '))
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
        # exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    print("Starting the CUYPY game...")
    welcome_message()
    menu()
        
if __name__ == "__main__":
    main()
    