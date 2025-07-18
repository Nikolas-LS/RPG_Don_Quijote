from Colors import colorText

def line():
    print(colorText.lightBlue('---' * 34))

def h():
    line()
    print(colorText.yellow('SESSÃO 3:'))
    print('''
    Don Quijote e sua fiel escudeira-jornalista chegam a um prédio coberto por 
    pichações e teias de aranha: a antiga Biblioteca Pública Municipal, agora 
    esquecida pela cidade que se embriaga em telas brilhantes e distrações 
    instantâneas. Ele acredita que ali repousa o Grimório da Verdade, um livro 
    sagrado capaz de despertar a humanidade da ilusão.

    Ao adentrar o local, encontra estantes semi-vazias, livros rasgados, páginas 
    queimadas... e, para sua surpresa, um pequeno grupo de jovens estudantes que, 
    em segredo, ainda se reúnem para “cultuar a sabedoria ancestral”. Eles o recebem 
    com reverência, acreditando estar diante de um visionário ou maluco inofensivo. 
    Inspirado, Don Quijote faz um juramento: "O mundo será restaurado pelas palavras 
    que ainda resistem!"

    Agora, com novos aliados e pistas ocultas nos livros resgatados, ele parte para um novo rumo.
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
    Inspirado pela ordem, Don Quijote lidera um protesto lírico. A polícia 
    dispersa o grupo com gás e cassetetes.Ele é silenciado junto com os 
    últimos versos da resistência.

    Final Ruim - A poesia morreu abafada pelo concreto.
    ''')
            line()
            exit()
        elif x == 3:
            # OPC ERRADA
            line()
            print('''
    Don Quijote tenta libertar mentes do “controle psíquico”, mas é capturado 
    e usado como cobaia. Dias depois, repete frases perfeitas... sem alma. 
    Ele agora acredita na ordem digital.

    Final Ruim - Você foi atualizado para a versão silenciosa.
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
    Inspirado pela ordem, Don Quijote lidera um protesto lírico. A polícia 
    dispersa o grupo com gás e cassetetes.Ele é silenciado junto com os 
    últimos versos da resistência.

    Final Ruim - A poesia morreu abafada pelo concreto.
    ''')
        line()
        exit()
    elif x == 3:
        # OPC ERRADA
        line()
        print('''
    Don Quijote tenta libertar mentes do “controle psíquico”, mas é capturado 
    e usado como cobaia. Dias depois, repete frases perfeitas... sem alma. 
    Ele agora acredita na ordem digital.

    Final Ruim - Você foi atualizado para a versão silenciosa.
    ''')
        line()
        exit()
    elif x == 0:
        # Sair do jogo
        print("Saindo do jogo...")
        exit()
