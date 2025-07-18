from Colors import colorText

def line():
    print(colorText.lightBlue('---' * 34))

def h():
    line()
    print(colorText.yellow('SESSÃO 2:'))
    print('''
    Após atravessar becos e viadutos, Don Quijote chega ao topo de um morro onde 
    ergue-se uma torre de transmissão cercada por muros, câmeras e placas dizendo 
    "Proibido entrar". Ele acredita estar diante do castelo do mago das ilusões, 
    o responsável por lançar imagens enganosas e palavras mágicas nas mentes das 
    pessoas. Lá dentro, operários controlam equipamentos que ele interpreta como 
    feitiçaria.

    Ao tentar invadir, é confundido com um manifestante maluco, mas foge com a 
    ajuda de uma jovem jornalista que acha sua causa... estranhamente inspiradora.

    Agora, ela o acompanha, e juntos decidem seu próximo destino. 
    ''')
    line()

def option(x):
    if x not in [0, 1, 2, 3]:
        while x not in [0, 1, 2, 3]:
            x = int(input(colorText.yellow("Opção inválida! Tente novamente: ")))
        if x == 2:
            # OPC CERTA
            print(colorText.green("Você escolheu a opção certa!\n"))
        elif x == 1:
            # OPC ERRADA
            line()
            print('''
    Ao tentar libertar os “prisioneiros do espetáculo”, Don Quijote se torna 
    o novo participante do reality. A audiência o adora... por rir dele.
    Sua missão vira entretenimento, e ele, um produto.

    Final Ruim - Você virou piada no horário nobre.
    ''')
            line()
            exit()
        elif x == 3:
            # OPC ERRADA
            line()
            print('''
    Don Quijote invade o prédio, buscando enfrentar os “dragões capitalistas”. 
    É preso por invasão e declarado mentalmente instável. Sua imagem vira 
    mascote de uma fintech: “Sonhe alto, lute mais.”

    Final Ruim - O sistema te comprou em prestações.
    ''')
            line()
            exit()
        elif x == 0:
            # Sair do jogo
            print("Saindo do jogo...")
            exit()
    elif x == 2:
        # OPC CERTA
        print(colorText.green("Você escolheu a opção certa!\n"))
    elif x == 1:
        # OPC ERRADA
        line()
        print('''
    Ao tentar libertar os “prisioneiros do espetáculo”, Don Quijote se torna 
    o novo participante do reality. A audiência o adora... por rir dele.
    Sua missão vira entretenimento, e ele, um produto.

    Final Ruim - Você virou piada no horário nobre.
    ''')
        line()
        exit()
    elif x == 3:
        # OPC ERRADA
        line()
        print('''
    Don Quijote invade o prédio, buscando enfrentar os “dragões capitalistas”. 
    É preso por invasão e declarado mentalmente instável. Sua imagem vira 
    mascote de uma fintech: “Sonhe alto, lute mais.”

    Final Ruim - O sistema te comprou em prestações.
    ''')
        line()
        exit()
    elif x == 0:
        # Sair do jogo
        print("Saindo do jogo...")
        exit()
