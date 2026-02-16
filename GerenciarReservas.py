import os
import time
from Database import dispositivos, horarios, salas, reservas
from GerenciarDispositivos import total_cadastrado
from MostrarReservas import mostrar_reservas
from paletadecores import *  # Importa as cores


#GERAR ID PARA RESERVA
contador_reservas = 1 + len(reservas)
def gerar_id_sequencial():
    global contador_reservas
    numero = contador_reservas
    contador_reservas += 1
    return numero


#FUNÇÕES UXILIARES PARA CONFIGURAR OPÇÕES DE RESERVAS


#Criar destino para usar aparelhos
def salvar_salas():
    i = 0
    print(f"\n{AZUL_BRILHANTE}==== Cadastro de Salas ===={RESET}")
    qtd_salas = int(input(f"{AZUL_CLARO}Quantas salas serão cadastradas: {RESET}"))
    while i < qtd_salas:
        sala = input(f"{CIANO}Insira o número ou nome da sala (ex: 'Sala 1' ou 'Laboratório'): {RESET}")
        salas.append(sala)
        i += 1  
    print(f"{AZUL_ESCURO}Salas cadastradas com sucesso!{RESET}")

    print(f"{AZUL_ESCURO}\t===== Salas cadastradas ====={RESET}")
    for sala in salas:
        print(f"{sala}")


#Criar horario de funcionamento
def definir_horario():
    global horarios

    horaI = 0
    horaF = 0

    print(f"\n{AZUL_BRILHANTE}==== Horário de funcionamento ===={RESET}")

    while horaI <= 0 or horaI > 24:
        horaI = int(input(f"{AZUL_CLARO}Insira o horário inicial (24h): {RESET}"))

    while horaF <= 0 or horaF > 24:
        horaF = int(input(f"{AZUL_CLARO}Insira o horário final (24h): {RESET}"))

        while horaF <= horaI:
            horaF = int(input(f"{VERMELHO}Final deve ser maior que o inicial. Tente novamente: {RESET}"))

    horarios = list(range(horaI, horaF + 1))
    print(f"{AZUL_CLARO}Horários cadastrados com sucesso!{RESET}")

    print(f"{AZUL_ESCURO}\t===== Horários cadastrados ====={RESET}")
    for hora in horarios:
        print(f"{hora}h")




#FUNÇÃO CONFIGURAR
def config_reservas():
    
    #MENU
    while True: 
        print(f"{AZUL_BRILHANTE}\t==== Configurações ===={RESET}")
        print(f"{AZUL_CLARO}1.{RESET} {BRANCO} Cadastrar destinos para usar aparelhos{RESET}")
        print(f"{AZUL_CLARO}2.{RESET} {BRANCO} Cadastrar horários para usar aparelhos{RESET}")
        print(f"{AZUL_CLARO}3.{RESET} {BRANCO} Sair{RESET}")

        menu = -1
        while menu not in [1,2,3]:
            menu = int(input(f"{AZUL_CLARO}Digite a opção escolhida: {RESET}"))
        if menu == 1:
            salvar_salas()
        elif menu == 2:
            definir_horario()
        elif menu == 3:
            break




#FUNÇÕES AUXILIARES PARA SELEÇÃO NA RESERVA


#Add horário
def escolher_horario():
    print(f"\n{AZUL_BRILHANTE}=== Opções de horário ==={RESET}")
    for i in horarios:
        print(f"{BRANCO}{i}:00{RESET}")

    hora_inicio = int(input(f"{AZUL_CLARO}Digite o horário inicial da reserva: {RESET}"))
    hora_fim = int(input(f"{AZUL_CLARO}Digite o horário final da reserva: {RESET}"))

    while not all(h in horarios for h in range(hora_inicio, hora_fim + 1)):
        print(f"{VERMELHO}Horário inválido ou fora do intervalo disponível.{RESET}")
        hora_inicio = int(input(f"{AZUL_CLARO}Digite o horário inicial: {RESET}"))
        hora_fim = int(input(f"{AZUL_CLARO}Digite o horário final: {RESET}"))

    return [hora_inicio, hora_fim]


#add sala
def escolher_sala():
    print(f"\n{AZUL_BRILHANTE}=== Opções de Salas ==={RESET}")
    for s in salas:
        print(f"{BRANCO}{s}{RESET}")

    sala = input(f"{AZUL_CLARO}Em qual sala será usado o aparelho? {RESET}")
    while sala not in salas:
        print(f"{VERMELHO}Sala inválida. Tente novamente.{RESET}")
        sala = input(f"{AZUL_CLARO}Em qual sala será usado o aparelho? {RESET}")

    return sala


#quantidade de aparelhos
def validar_quantidade(total_cadastrado):
    total_emprestar = int(input(f"\n{AZUL_CLARO}Quantos aparelhos deseja emprestar? (máx: {total_cadastrado}): {RESET}"))
    while total_emprestar > total_cadastrado or total_emprestar <= 0:
        print(f"{VERMELHO}Quantidade inválida.{RESET}")
        total_emprestar = int(input(f"{AZUL_CLARO}Digite um valor entre 1 e {total_cadastrado}: {RESET}"))
    return total_emprestar


#listar aparelhos
def listar_aparelhos_disponiveis():
    disponiveis = []
    print(f"\n{AZUL_BRILHANTE}=== Aparelhos disponíveis ==={RESET}")
    for marca, lista in dispositivos.items():
        for aparelho in lista:
            if aparelho["status"] == "disponível":
                print(f"Código: {BRANCO}{aparelho['codigo']:<20}{RESET} | Marca: {BRANCO}{marca:<20}{RESET} | Modelo: {BRANCO}{aparelho['modelo']:<20}{RESET} | Status: {AZUL_CLARO}{aparelho['status']:<20}{RESET}")
                disponiveis.append(aparelho["codigo"])
    return disponiveis


#selecionar aparelhos
def selecionar_aparelhos(disponiveis, total_emprestar):
    reservado = []
    print(f"\n{AZUL_BRILHANTE}Selecionar aparelhos:{RESET}")
    for i in range(total_emprestar):
        emprestar = ""
        while emprestar not in disponiveis or emprestar in reservado:
            emprestar = input(f"{AZUL_CLARO}Insira o código do aparelho: {RESET}")
            if emprestar not in disponiveis:
                print(f"{VERMELHO}Código inválido ou indisponível.{RESET}")
            elif emprestar in reservado:
                print(f"{VERMELHO}Este aparelho já foi selecionado.{RESET}")
        reservado.append(emprestar)
        for marca, lista in dispositivos.items():
            for aparelho in lista:
                if aparelho["codigo"] == emprestar:
                    aparelho["status"] = "indisponível"
                    break
    return reservado



#CRIAR EMPRÉSTIMO
def criar_reserva():
    global reservas
    ID = gerar_id_sequencial()


    hora = escolher_horario()
    sala = escolher_sala()
    total_emprestar = validar_quantidade(total_cadastrado())
    disponiveis = listar_aparelhos_disponiveis()
    reservado = selecionar_aparelhos(disponiveis, total_emprestar)

    reservas[ID] = {
        "Hora": hora,
        "Destino": sala,
        "Código": reservado
    }

    print(f"\n{AZUL_BRILHANTE}Reserva criada com sucesso!{RESET}")
    print(f"{AZUL_CLARO}ID: {BRANCO}{ID}{RESET}")
    print(reservas[ID])



#FUNÇÃO EDITAR EMPRÉSTIMO

def editor_reserva():

    print(f"\n{AZUL_BRILHANTE}=== Reservas Atuais ==={RESET}")
    for id_reserva in reservas:
        print(f"ID: {BRANCO}{id_reserva}{RESET}")

    reserva_id = input("\nDigite o ID da reserva que deseja editar: ")
    while reserva_id not in reservas:
        print("Reserva não encontrada!")
        # print(reserva_id)
        # print(reservas)
        reserva_id = input("Digite o ID da reserva que deseja editar: ")

    dados = reservas[reserva_id]

    while True:
        print("\n--- Informações atuais da reserva ---")
        print(f"Hora: {dados['Hora']}")
        print(f"Destino: {dados['Destino']}")
        print(f"Quantidade: {len(dados['Código'])}")
        print(f"Códigos: {dados['Código']}")

        print("\nComandos:")
        print("e -> editar")
        print("s -> sair e salvar")

        comando = input("Digite o comando: ").lower()

        if comando == "e":
            while True:

                print("\n--- Escolha uma opção para alterar ---")
                print(f"1. Hora")
                print(f"2. Destino")
                print(f"3. Alterar todos aparelhos")
                print(f"4. Substituir um aparelho")

                num_linha = input("Digite a opção (1-4) que deseja editar: ")
                if num_linha in ["1", "2", "3", "4"]:
                    break
                else:
                    print("Número inválido! Por favor digite 1, 2, 3 ou 4")

            # edita horários
            if num_linha == "1":
                while True:
                    print(horarios)
                    hora = input("Digite os horários separados por espaço (ex: 8 10): ")
                    partes = hora.strip().split()

                    if len(partes) != 2 or not all(p.isdigit() for p in partes):
                        print("Entrada inválida!")
                        continue

                    hora_inicio, hora_fim = map(int, partes)

                    if hora_inicio not in horarios or hora_fim not in horarios or hora_inicio >= hora_fim:
                        print("Horário inválido! Tente novamente.")
                        continue

                    dados["Hora"] = [hora_inicio, hora_fim]
                    print("Horário atualizado com sucesso!")
                    break

            # edita salas
            elif num_linha == "2":
                print("\n--- Opções de salas ---")
                for sala in salas:
                    print(sala)
                destino = input("Em qual sala será usado o aparelho? ").capitalize()
                while destino not in salas:
                    print("Local inválido!")
                    destino = input("Em qual sala será usado o aparelho? ").capitalize()
                dados["Destino"] = destino
                print("Destino atualizado com sucesso!")

                # edita quantidades
            elif num_linha == "3":
                 novo_total = validar_quantidade(total_cadastrado())
                 lista_disponivel = listar_aparelhos_disponiveis()
                 print(lista_disponivel)
                 codigo = selecionar_aparelhos(lista_disponivel, novo_total)
                 dados["Código"] = codigo

            # edita os códigos
            elif num_linha == "4":
                valor_atual = dados["Código"]
                print("Códigos atuais:")
                codes = []
                for codigo in dados["Código"]:
                    codes.append(codigo)
                    print(codigo)
                    print(codes)

                old_code = input("Digite o código que quer editar: ")
                index = dados["Código"].index(old_code)
                if old_code not in codes:
                    print("Insira um código válido!")
                    while old_code not in codes:
                        mudar_code = input("Digite o número do código que quer editar: ")
                else:
                    listar_aparelhos_disponiveis()
                    substituido = selecionar_aparelhos(listar_aparelhos_disponiveis(),1)
                    dados["Código"][index] = substituido[0]


            else:
                    print("Opção inválida!")

        elif comando == "s":
            print("Alterações salvas com sucesso!")
            break

        else:
            print("Comando inválido!")



#CANCELAR EMPRÉSTIMO
def cancelar_reserva():

    if not reservas:
        print("\n⚠️ Nenhuma reserva cadastrada.")
        return

    print("\n=== Reservas Cadastradas ===")
    for id_reserva, dados in reservas.items():
        print(f"\nID: {id_reserva}")
        print(f"  Horário: {dados['Hora'][0]}h às {dados['Hora'][1]}h")
        print(f"  Destino: {dados['Destino']}")
        print(f"  Aparelhos: {', '.join(dados['Código'])}")

    reserva_id = input("\nDigite o ID da reserva que deseja cancelar: ").strip()

    if reserva_id not in reservas:
        print("❌ Reserva não encontrada!")
        return

    confirm = input(f"Tem certeza que deseja cancelar a reserva '{reserva_id}'? (s/n): ").strip().lower()

    if confirm == 's':
        del reservas[reserva_id]
        print("✅ Reserva cancelada com sucesso!")
    else:
        print("❎ Cancelamento abortado.")




#MENU RESERVAS
def menu_reservas():
    os.system('cls' if os.name == 'nt' else 'clear')            

    escolha = -1
    while escolha != 5:
        # Exibir opções
        print(f"{AZUL_BRILHANTE}{'+'+'='*30}\n{'MENU PRINCIPAL':^30}\n{'='*30 +'+'}{RESET}")
        print(f"{AZUL_CLARO}0. Configurar empréstimos{RESET}")
        print(f"{AZUL_CLARO}1. Criar empréstimos{RESET}")
        print(f"{AZUL_CLARO}2. Mostrar empréstimo{RESET}")
        print(f"{AZUL_CLARO}3. Editar empréstimo{RESET}")
        print(f"{AZUL_CLARO}4. Cancelar empréstimo{RESET}")
        print(f"{AZUL_CLARO}5. Sair{RESET}")

        escolha = int(input("Digite a sua opcao: "))

        # Verificar se a opção está no intervalo válido
        if escolha < 0 or escolha > 5:
            print(f"{VERMELHO}\tVocê digitou um valor inválido!\n{RESET}")
            continue

        # Executar ação com base na escolha
        if escolha == 0:
            os.system('cls' if os.name == 'nt' else 'clear')            
            config_reservas()
            os.system('cls' if os.name == 'nt' else 'clear')
        if escolha == 1:
            os.system('cls' if os.name == 'nt' else 'clear')            
            criar_reserva()
        elif escolha == 2:
            os.system('cls' if os.name == 'nt' else 'clear')            
            mostrar_reservas()
            input("Pressione uma tecla para voltar ao menu")

        elif escolha == 3:
            os.system('cls' if os.name == 'nt' else 'clear')            
            editor_reserva()
        elif escolha == 4:
            os.system('cls' if os.name == 'nt' else 'clear')            
            cancelar_reserva()
        else:
            print(f"{AZUL_ESCURO}Voltando para o menu principal...{RESET}")
            time.sleep(2)






