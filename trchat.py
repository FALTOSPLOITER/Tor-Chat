def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     #######    
      _ ___ _   _ ____  ____  _     ___ ___ _____ _____ ____  
     | |_ _| \ | / ___||  _ \| |   / _ \_ _|_   _| ____|  _ \ 
  _  | || ||  \| \___ \| |_) | |  | | | | |  | | |  _| | |_) |
 | |_| || || |\  |___) |  __/| |__| |_| | |  | | | |___|  _ < 
  \___/|___|_| \_|____/|_|   |_____\___/___| |_| |_____|_| \_|
                                                                  
JINSPLOITER: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
    """)

def Main():
    home_logo()
    print("1\tStart Server\n2\tConnect with server")
    select = int(input("Select ::: "))
    if select == 1:
        import server
    elif select == 2:
        import client
    else:
        print("Please choose 1 or 2")

if __name__ == "__main__":
    Main()
