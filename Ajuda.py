import os
from paletadecores import * 


def manual():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f"""
{AZUL_ESCURO}=====================================================================
                      {BRANCO}{NEGRITO}BEM-VINDO À VERSÃO 1.0 DO iTRACK{RESET}
{AZUL_ESCURO}====================================================================={RESET}

{CIANO}Nossa ferramenta tem como objetivo gerenciar o empréstimo de 
equipamentos da sua instituição.

{AZUL_CLARO}Informamos que essa é uma VERSÃO BETA do programa e, portanto, é 
recomendado para ambientes de BAIXA DEMANDA.

{BRANCO}⚠ Atenção: Toda vez que a pessoa abrir o programa, ela deverá inserir 
novamente os aparelhos, pois os dados não são salvos ao fechar.{RESET}

{CIANO}Para fazer sugestões de implementação em futuras versões, contate: 
          software_empresa@gmail.com

Atenciosamente,  
Equipe desenvolvedora

{AZUL_ESCURO}=====================================================================
                          {NEGRITO}MANUAL DE USO
{AZUL_ESCURO}====================================================================={RESET}


{AZUL_CLARO}=====================
 MENU: OPÇÕES
====================={RESET}
1. Aparelhos Registrados  
2. Reservar Aparelho  
3. Mostrar Reservas do Dia


{AZUL_CLARO}=====================
 OPÇÃO 1: APARELHOS REGISTRADOS
====================={RESET}
- Lista de equipamentos operando (classificados por MARCA).  
- Mostra o STATUS dos computadores:  
    -> Disponível  
    -> Indisponível  

Alterações possíveis:  
- Cadastrar novo dispositivo.  
- Adicionar dispositivo à lista de manutenção.  
- Alterar o status do dispositivo.


{AZUL_CLARO}=====================
 OPÇÃO 2: RESERVAR APARELHO
====================={RESET}
Permite fazer uma reserva informando:  
- DESTINO (Ex.: sala de aula onde o aparelho será usado).  
- PERÍODO DE RESERVA (Ex.: bloco de aula - 1ª, 2ª, 3ª aula...).  
- QUANTIDADE e CÓDIGO dos aparelhos registrados.  

O sistema verifica se o aparelho está disponível antes de concluir  
a reserva.


{AZUL_CLARO}=====================
 OPÇÃO 3: MOSTRAR RESERVAS DO DIA
====================={RESET}
- Mostra, dividido pelos blocos (1ª, 2ª, 3ª aula...), os aparelhos  
reservados no dia.  

Atenção:  
- Essa tela é apenas para CONSULTA.  
- Não é possível realizar alterações, cancelamentos ou criar reservas  
a partir dessa opção.


{AZUL_CLARO}=====================
 DICAS IMPORTANTES
====================={RESET}
✔ Verifique sempre o STATUS dos equipamentos antes de reservar.  
✔ Equipamentos em manutenção aparecem como INDISPONÍVEIS.  
✔ Use corretamente o CÓDIGO dos aparelhos na hora de reservar.  
✔ Consulte as reservas do dia para evitar conflitos e sobreposição.  
{BRANCO}✔ 🔴 IMPORTANTE: Toda vez que abrir o programa, você precisará 
cadastrar novamente os aparelhos, pois os dados não ficam salvos após 
fechar.{RESET}

{AZUL_ESCURO}=====================================================================
                       {NEGRITO}FIM DO MANUAL DE USO
{AZUL_ESCURO}====================================================================={RESET}
""")
