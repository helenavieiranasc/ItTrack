from Database import reservas, horarios
from paletadecores import *  # Importa as cores


def mostrar_reservas():
    print(f"\n{AZUL_BRILHANTE}--- RESERVAS ---{RESET}")
    for reserva_id, dados in reservas.items():
        print(f"\n{AZUL_CLARO}ID da reserva: {BRANCO}{reserva_id}{RESET}")
        for chave, valor in dados.items():
            print(f"{CIANO}{chave}: {BRANCO}{valor}{RESET}")



def reservas_matriz(horarios, reservas):

    if len(reservas) == 0:
        print("Nenhuma reserva cadastrada.")
        return

    #cabeçalho
    margem = " " * 6
    


    reservantes_por_hora = {
        h: [k for k, v in reservas.items() if h in v.get("Hora", [])]
        for h in horarios
    }

    max_colunas = max(len(reservantes) for reservantes in reservantes_por_hora.values()) + 2
    
    divisoria_horizontal = "+" + max_colunas*("-"*8+"+")


    largura = len(divisoria_horizontal) - 2

    print()
    print(f"{margem}+{'=' * largura}+")
    print(f"{margem}|{'RESERVAS POR HORÁRIO'.center(largura)}|")
    print(f"{margem}+{'=' * largura}+")
    
    legenda = f"{margem}|{'Horário':>8}|{'Qtd':>8}| Reservas{(largura - 27)*' '}|"
    
    print(legenda)
    print(margem+divisoria_horizontal)

    if all(len(reservantes) == 0 for reservantes in reservantes_por_hora.values()):
        print("Nenhuma reserva encontrada.")
        return
        
    for horario in horarios:
        print("      ", end="")
        reservantes = reservantes_por_hora[horario]
        aux = ''
        for reserva in reservantes:
            aux += f"ID: {reserva:>4}|"
        linha = f"|{horario:>7}h|{len(reservantes):>8}|{aux}"
        largura_esperada = largura + 2
        if len(linha) < largura_esperada:
            linha += (largura_esperada - len(linha) - 1)*" " + '|'
        print(linha)

    print(margem+divisoria_horizontal)


#MENU MOSTRAR RESERVAS
def menu_mostrar_reservas():

    reservas_matriz(horarios, reservas)

    escolha = "y"

    print("\n\tMais informações...")
    while escolha not in list["s","n"]:
        escolha = input("Deseja ver os dados de todas as reservas cadastradas? (s/n): ")
        print()
        if escolha == "s":
            mostrar_reservas()
        else:
            break
                       
