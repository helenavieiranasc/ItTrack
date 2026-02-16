from Database import dispositivos, horarios, salas, reservas
from MostrarReservas import mostrar_reservas


horario_de_funcionamento = list(range(8, 11 + 1)) # ! Funciona das 8h as 11h
for i in horario_de_funcionamento:
    horarios.append(i)
    
def addDispositivo(marca, modelo, qtd):
    marca = marca.upper()
    dispositivos.setdefault(marca, [])
    num_inicial = len(dispositivos[marca]) + 1
    for i in range(qtd):
        serial = str(num_inicial + i).zfill(8)
        codigo = f"{marca}{serial}"
        dispositivos[marca].append({
                    "codigo": codigo,
                    "modelo": modelo,
                    "status": "disponível"
                })


def addSala(nome):
    salas.append(nome)

def addReserva(ID, horaInicio, horaFinal, sala, reservado):
    reservas[str(ID)] = { # ID = Qualquer id pra representar a reserva
            "Hora": [horaInicio, horaFinal], # Dois inteiros entre os horários disponíveis (nesse caso entre as 8h e 11h)
            "Destino": sala, # Qualquer string com um dos valores a seguir: ["Sala 01", "Sala 02", "Sala 03", "Sala 04", "Sala 05", "Sala 06", "Sala 07", "Sala 08", "Sala 09", Cozinha]
            "Código": [reservado] # Formato do código: {marca em CAPSLOCK}{número incremental de exatos 8 dígitos (zeros adicionados a esquerda)}
        }
    
    for marca, dispositivo_lista in dispositivos.items():
        for dispositivo in dispositivo_lista:
            if dispositivo["codigo"] == reservado:
                dispositivo["status"] = "indisponível"


    
# ! Começando a feedar

# * Dispositivos

# Notebooks
addDispositivo("Dell", "XPS 15", 15)
addDispositivo("Apple", "MacBook Pro 14", 12)
addDispositivo("Lenovo", "ThinkPad X1 Carbon", 20)
addDispositivo("HP", "Spectre x360", 10)

# Smartphones
addDispositivo("Apple", "iPhone 15 Pro", 25)
addDispositivo("Samsung", "Galaxy S25 Ultra", 22)
addDispositivo("Google", "Pixel 9 Pro", 18)

# Tablets
addDispositivo("Apple", "iPad Pro 12.9", 30)
addDispositivo("Samsung", "Galaxy Tab S9", 15)
addDispositivo("Microsoft", "Surface Pro 9", 12)

# Câmeras
addDispositivo("Sony", "Alpha A7 IV", 8)
addDispositivo("Canon", "EOS R6 Mark II", 7)
addDispositivo("Nikon", "Z8", 5)

# Projetores
addDispositivo("Epson", "Home Cinema 3800", 10)
addDispositivo("BenQ", "TK700", 8)

# Drones
addDispositivo("DJI", "Mavic 3 Pro", 6)
addDispositivo("DJI", "Air 3", 10)


# * Local

addSala("Sala 01")
addSala("Sala 02")
addSala("Sala 03")
addSala("Sala 04")
addSala("Sala 05")
addSala("Sala 06")
addSala("Sala 07")
addSala("Sala 08")
addSala("Sala 09")
addSala("Cozinha")

# * Reserva

# ID: 1 - Reservando o primeiro notebook Dell
addReserva(1, 8, 10, "Sala 01", "DELL00000001")

# ID: 2 - Reservando o primeiro MacBook Pro
addReserva(2, 9, 11, "Sala 03", "APPLE00000001")

# ID: 3 - Reservando o primeiro iPhone
addReserva(3, 8, 9, "Sala 02", "APPLE00000004")

# ID: 4 - Reservando a primeira câmera Sony para uma sessão na Cozinha
addReserva(4, 10, 11, "Cozinha", "SONY00000001")

# ID: 5 - Reservando o único drone DJI
addReserva(5, 8, 11, "Sala 08", "DJI00000001")

# ID: 6 - Reservando o segundo notebook Dell
addReserva(6, 9, 10, "Sala 05", "DELL00000002")

# ID: 7 - Reservando o segundo MacBook Pro para uma longa sessão de edição
addReserva(7, 8, 11, "Sala 03", "APPLE00000002")

# ID: 8 - Reservando o segundo iPhone para uma demonstração rápida
addReserva(8, 10, 11, "Sala 06", "APPLE00000005")

# ID: 9 - Reservando a segunda câmera Sony
addReserva(9, 8, 9, "Sala 04", "SONY00000002")

# ID: 10 - Reservando o terceiro iPhone disponível
addReserva(10, 9, 10, "Sala 02", "APPLE00000006")

# addReserva(11, 8, 9, "Cozinha", "APPLE00000008")

def mostrar_disponivel():
    for marca, dispositivolista in dispositivos.items():
        for elemento in dispositivolista:
                if elemento["status"] == "disponível":
                    print(elemento)

def mostrar_indisponivel():
    for marca, dispositivolista in dispositivos.items():
        for elemento in dispositivolista:
                if elemento["status"] == "indisponível":
                    print(elemento)

def search_dispositivo(key, value):
    for marca, dispositivolista in dispositivos.items():
            for elemento in dispositivolista:
                    if elemento[key] == value:
                        print(elemento)


from main import main

main()


