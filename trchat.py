def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     #######        
        
  ______      _   _______ ____   _____ _____  _      ____ _____ _______ ______ _____  
 |  ____/\   | | |__   __/ __ \ / ____|  __ \| |    / __ \_   _|__   __|  ____|  __ \ 
 | |__ /  \  | |    | | | |  | | (___ | |__) | |   | |  | || |    | |  | |__  | |__) |
 |  __/ /\ \ | |    | | | |  | |\___ \|  ___/| |   | |  | || |    | |  |  __| |  _  / 
 | | / ____ \| |____| | | |__| |____) | |    | |___| |__| || |_   | |  | |____| | \ \ 
 |_|/_/    \_\______|_|  \____/|_____/|_|    |______\____/_____|  |_|  |______|_|  \_\
                                                                                      
FALTOSPLOITER: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
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
