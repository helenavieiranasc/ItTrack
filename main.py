import os
from MenuPrincipal import menu_principal, titulo_custom

def main():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(titulo_custom)
    menu_principal()

main()