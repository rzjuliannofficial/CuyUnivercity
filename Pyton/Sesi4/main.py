from libs import welcome_message
from games import cuypy

def main():
    welcome_message("WELCOME TO CUYPY GAME")
    cuypy.start()
    
if __name__ == "__main__":
    print("Starting the CUYPY game...")
    main()