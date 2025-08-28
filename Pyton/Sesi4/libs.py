import socket
from time import sleep

pc_name = socket.gethostname()

def welcome_message():
    star = "*" * (len(pc_name) + 6)
    print(star)
    print(f"** {pc_name} **")
    print(star)
    
def exit_program():
    print("Exiting the program...")
    i=3
    while i>0:
        print(f"{i}...")
        i-=1
        sleep(1)
    print("Goodbye!")
    # exit()

if __name__ == "__main__":
    welcome_message()
    exit_program()
    