from Colors import colorText

def line():
    print(colorText.lightBlue('---' * 34))

def h():
    line()
    print(colorText.yellow('SESSÃO 1:'))
    print('''     
    Don Quijote desperta em meio ao tumulto da Estação Central de São Paulo, 
    acreditando estar em uma fortaleza sitiada por forças do caos. As luzes 
    fluorescentes o confundem, os alto-falantes são vozes proféticas, e os 
    seguranças, sentinelas de um reino sombrio. Ele ouve gritos de uma criança, 
    vê um homem sendo ignorado ao pedir ajuda, e sente que a injustiça está 
    em toda parte. Com lança improvisada em mãos (um cabo de vassoura), 
    jura: “Este reino será purificado!”
    ''')
    line()

def option(x):
    if x not in [0, 1, 2, 3]:
        while x not in [0, 1, 2, 3]:
            x = int(input(colorText.yellow("Opção inválida! Tente novamente: ")))
        if x == 1:
            # OPC CERTA
            print(colorText.green("Você escolheu a opção certa!\n"))
        elif x == 2:
            # OPC ERRADA
            line()
            print('''
    Don Quijote tenta libertar as “almas aprisionadas” no templo do consumo, 
    mas é confundido com um assaltante. Imobilizado pelos seguranças, é zombado 
    por clientes que filmam sua “loucura”. 
    Torna-se viral como "O cavaleiro Black Friday".

    Final Ruim – Você foi derrotado por um cartão de crédito.
    ''')
            line()
            exit()
        elif x == 3:
            # OPC ERRADA
            line()
            print('''
    Don Quijote decide enfrentar os "senhores cruéis", mas entra em conflito 
    com traficantes reais. Sua armadura improvisada não resiste a balas. É 
    deixado como um corpo estranho em um lugar esquecido.

    Final Ruim - A justiça romântica não sobreviveu à realidade crua.
    ''')
            line()
            exit()
        elif x == 0:
            # Sair do jogo
            print("Saindo do jogo...")
            exit()
    elif x == 1:
        # OPC CERTA
        print(colorText.green("Você escolheu a opção certa!\n"))
    elif x == 2:
        # OPC ERRADA
        line()
        print('''
    Don Quijote tenta libertar as “almas aprisionadas” no templo do consumo, 
    mas é confundido com um assaltante. Imobilizado pelos seguranças, é zombado 
    por clientes que filmam sua “loucura”. 
    Torna-se viral como "O cavaleiro Black Friday".

    Final Ruim – Você foi derrotado por um cartão de crédito.
    ''')
        line()
        exit()
    elif x == 3:
        # OPC ERRADA
        line()
        print('''
    Don Quijote decide enfrentar os "senhores cruéis", mas entra em conflito 
    com traficantes reais. Sua armadura improvisada não resiste a balas. É 
    deixado como um corpo estranho em um lugar esquecido.

    Final Ruim – A justiça romântica não sobreviveu à realidade crua.
    ''')
        line()
        exit()
    elif x == 0:
        # Sair do jogo
        print("Saindo do RPG...")
        exit()
