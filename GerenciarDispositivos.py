import os
import time
from Database import dispositivos
from paletadecores import *  # Importa as cores



#CADASTRAR EQUIPAMENTOS
def cadastro_dispositivos():

    print(f"{NEGRITO}{AZUL_BRILHANTE}         +====Bem vindo ao Sistema itTrack====+{RESET}")
    print(f"{CIANO}    Primeiramente você irá inserir os dados, ou seja, marca, modelo e quantidade.{RESET}")

    while True:
        marca = input(f"{AZUL_CLARO}Marca: {RESET}").strip().upper()
        modelo = input(f"{AZUL_CLARO}Modelo: {RESET}").strip()
        quantidade = int(input(f"{AZUL_CLARO}Quantidade: {RESET}"))        
        dispositivos.setdefault(marca, [])
        num_inicial = len(dispositivos[marca]) + 1

        for i in range(quantidade): 
            serial = str(num_inicial + i).zfill(8)
            codigo = f"{marca}{serial}"
            dispositivos[marca].append({
                "codigo": codigo,
                "modelo": modelo,
                "status": "disponível"

            })
            print(f"{AZUL_CLARO}📦 Dispositivo cadastrado: {AZUL_ESCURO}{codigo}{RESET}")

        continuar = input(f"\n{CIANO}Quer cadastrar outra marca? (s para sim / n para não): {RESET}").lower().strip()
        if continuar != "s": 
            break

def total_cadastrado():
    total = sum(len(lista) for lista in dispositivos.values())
    return total




#EDITAR APARELHOS CADASTRADOS

def editar_aparelho():

    mostrar_aparelhos()
    marca_antiga = input("Digite a marca que deseja alterar: ").strip().upper()

    if marca_antiga not in dispositivos:
        print("Marca não encontrada.!!")

        return

    modelos_unicos = set(d['modelo'] for d in dispositivos[marca_antiga])
    print("\nModelos disponíveis dessa marca:")
    for modelo in modelos_unicos:
        print(f"- {modelo}")

    modelo_antigo = input("Digite o modelo que deseja substituir: ").strip()
    nova_marca = input("Nova marca: ").strip().upper()
    novo_modelo = input("Novo modelo: ").strip()
    nova_lista = []
    i = 1
    qtde_str = input("Quantidade do novo lote: ").strip()
    if not qtde_str.isdigit():  
        print("Quantidade inválida. Operação cancelada.")
        return
    nova_quantidade = int(qtde_str)
    nova_lista = []
    for i in range(1, nova_quantidade + 1):
        codigo = nova_marca + str(i).zfill(8)
        nova_lista.append({
            "codigo": codigo,
            "modelo": novo_modelo,
            "status": "disponível"
        })

    dispositivos[marca_antiga] = [d for d in dispositivos[marca_antiga] if d["modelo"] != modelo_antigo]
    if not dispositivos[marca_antiga]:
        del dispositivos[marca_antiga]
    dispositivos.setdefault(nova_marca, []).extend(nova_lista)
    print(f"{len(nova_lista)} aparelho(s) alterado(s) com sucesso.")



#MOSTRAR APARELHOS CADASTRADOS 
def mostrar_aparelhos():
    if not dispositivos:
        print(f"{VERMELHO}⚠️ Nenhum aparelho cadastrado.{RESET}")
        return

    print(f"{NEGRITO}{AZUL_BRILHANTE}\n+==== Lista de Aparelhos Cadastrados ====+{RESET}")
    for marca, lista in dispositivos.items():
        print(f"\n{NEGRITO}{AZUL_CLARO}Marca: {marca}{RESET}")
        print(f"{'CÓDIGO':<15} | {'MODELO':<20} | {'STATUS':<12}")
        print("-" * 55)
        for d in lista:
            print(f"{d['codigo']:<15} | {d['modelo']:<20} | {d['status']:<12}")

#EXCLUIR APARELHOS
def excluir_aparelhos(dispositivos):
    mostrar_aparelhos()

    marca = input("Digite a marca do aparelho que deseja excluir: ").strip().upper()

    if marca not in dispositivos or not dispositivos[marca]:
        print("Marca não encontrada ou sem aparelhos cadastrados.")
        return

    nome_aparelho = input("Digite o codigo do aparelho que deseja excluir: ").strip()
    
    lista = dispositivos[marca]
    lista.sort(key=lambda x: x["codigo"])

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        modelo_meio = lista[meio]["codigo"]

        if modelo_meio == nome_aparelho:
            lista.pop(meio)
            print(f"Aparelho '{nome_aparelho}' da marca '{marca}' removido com sucesso!!")
            
            if not lista:
                del dispositivos[marca]
            return
        elif nome_aparelho < modelo_meio:
            fim = meio - 1
        else:
            inicio = meio + 1

    print(f"Aparelho '{nome_aparelho}' não encontrado na marca '{marca}'.")

def cabecalho(titulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{NEGRITO}{AZUL_BRILHANTE}+{'='*10} {titulo} {'='*10}+{RESET}")

#MENU GERENCIAR
def menu_gerenciar():
    escolha = -1
    while escolha != 5:
        cabecalho("Menu de Gerenciamento de Aparelhos")
        print(f"{AZUL_ESCURO}1.{RESET} {BRANCO}Adicionar aparelhos{RESET}")
        print(f"{AZUL_ESCURO}2.{RESET} {BRANCO}Mostrar aparelhos{RESET}")
        print(f"{AZUL_ESCURO}3.{RESET} {BRANCO}Editar aparelhos{RESET}")
        print(f"{AZUL_ESCURO}4.{RESET} {BRANCO}Excluir aparelhos{RESET}")
        print(f"{AZUL_ESCURO}5.{RESET} {BRANCO}Sair{RESET}")

        escolha = int(input(f"{AZUL_CLARO}Digite a sua opção: {RESET}"))

        if escolha < 1 or escolha > 5:
            print(f"{VERMELHO}⚠️ Digite um número válido.{RESET}")
            continue

        if escolha == 1:
            os.system('cls' if os.name == 'nt' else 'clear')            
            cadastro_dispositivos()
        elif escolha == 2:
            os.system('cls' if os.name == 'nt' else 'clear')            
            mostrar_aparelhos()
            input("Pressione alguma tecla para voltar ao menu")
            os.system('cls' if os.name == 'nt' else 'clear')            

        elif escolha == 3:
            os.system('cls' if os.name == 'nt' else 'clear')            
            editar_aparelho()
            input("Pressione alguma tecla para voltar ao menu")
        elif escolha == 4:
            os.system('cls' if os.name == 'nt' else 'clear')            
            excluir_aparelhos(dispositivos)
        else:           
            print(f"{AZUL_BRILHANTE}🔙 Voltando para o menu principal...{RESET}")
            time.sleep(2)


