import os
import time
from paletadecores import *  # Importa as cores
from Devoluções import devolver_equipamento
from GerenciarDispositivos import menu_gerenciar
from GerenciarReservas import menu_reservas, mostrar_reservas
from MostrarReservas import menu_mostrar_reservas
from Database import horarios, reservas
from Ajuda import manual


titulo_custom = f"""\t{FUNDO_PRETO}{AZUL_BRILHANTE}{NEGRITO}

  _ _ _______             _    
 (_) |__   __|           | |   
  _| |_ | |_ __ __ _  ___| | __
 | | __|| | '__/ _` |/ __| |/ /
 | | |_ | | | | (_| | (__|   < 
 |_|\__||_|_|  \__,_|\___|_|\_\



{BRANCO}+CONTROLE DE PATRIMÔNIO ELETRÔNICO+{AZUL_BRILHANTE}{RESET}
"""


def menu_principal():
    escolha = -1
    while escolha != 6:
        print(f"{AZUL_ESCURO}{NEGRITO}=============== MENU PRINCIPAL ==============={RESET}")
        print(f"{AZUL_BRILHANTE}1.{RESET} {BRANCO}Mostrar empréstimos{RESET}")
        print(f"{AZUL_BRILHANTE}2.{RESET} {BRANCO}Gerenciar equipamentos{RESET}")
        print(f"{AZUL_BRILHANTE}3.{RESET} {BRANCO}Gerenciar empréstimos{RESET}")
        print(f"{AZUL_BRILHANTE}4.{RESET} {BRANCO}Devolver aparelhos{RESET}")
        print(f"{AZUL_BRILHANTE}5.{RESET} {BRANCO}Ajuda{RESET}")
        print(f"{AZUL_BRILHANTE}6.{RESET} {BRANCO}Sair{RESET}")

        escolha = int(input(f"{CIANO}Digite a sua opção: {RESET}"))

        if escolha < 1 or escolha > 6:
            print(f"{VERMELHO}⚠ Por favor, digite um número válido!{RESET}")
            continue

        if escolha == 1:
            menu_mostrar_reservas()
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 2:
            menu_gerenciar()
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 3:
            menu_reservas()
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 4:
            devolver_equipamento()
            input("Pressione uma tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            
        elif escolha == 5:
            manual()
            input("Pressione uma tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear') 
            print(f"{AZUL_BRILHANTE}Saindo...{RESET}")
        else:
            exit()



