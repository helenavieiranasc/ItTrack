from Database import reservas

def devolver_equipamento():
    if not reservas:
        print("\n⚠️ Nenhuma reserva cadastrada.")
        return

    print("\n=== Reservas Cadastradas ===")
    for id_reserva, dados in reservas.items():
        print(f"\nID: {id_reserva}")
        print(f"  Horário: {dados['Hora'][0]}h às {dados['Hora'][1]}h")
        print(f"  Destino: {dados['Destino']}")
        print(f"  Aparelhos: {', '.join(dados['Código'])}")

    reserva_id = input("\nDigite o ID de empréstimo que deseja devovler: ").strip()

    if reserva_id not in reservas:
        print("❌ Empréstimo não encontrado!")
        return

    confirm = input(f"Tem certeza que deseja devolver '{reserva_id}'? (s/n): ").strip().lower()

    if confirm == 's':
        del reservas[reserva_id]
        print("✅ Devolução sucedida!")
    else:
        print("❎ Devolução abortada.")