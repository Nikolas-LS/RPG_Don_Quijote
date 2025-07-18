from Colors import colorText

def line():
    print(colorText.lightBlue('---' * 34))

def h():
    line()
    print(colorText.yellow('SESSÃO FINAL:'))
    print('''
    Don Quijote, guiado por fragmentos de sabedoria esquecida e ajudado por jovens idealistas, 
    chega ao Centro Nacional de Curadoria de Informação, um edifício frio e sem janelas, que 
    ele enxerga como a Torre dos Ilusionistas — o coração da manipulação moderna. Convencido de 
    que ali está guardado o Livro das Mentiras, um grimório digital que reescreve a realidade, 
    ele decide enfrentar os "escribas do mal" e libertar a verdade.

    Armado com sua lança improvisada e seu fervor idealista, Don Quijote invade o local, 
    sendo rapidamente confundido com um protestante insano. Enquanto sua escudeira transmite 
    tudo pela internet, ele confronta o Mestre dos Espelhos, uma inteligência artificial que 
    decide o que o povo pode ver, dizer e lembrar.

    Mesmo prestes a ser detido, Don Quijote brada com coragem trechos de Cervantes, 
    manifestos de rebeldia e o "Código da Imaginação". Suas palavras rompem o silêncio 
    digital e viralizam, despertando a juventude para questionar as verdades impostas.

    Don Quijote é capturado — mas não silenciado.
    Sua figura renasce como símbolo de resistência em murais urbanos, fóruns livres 
    e entre aqueles que ainda ousam imaginar um mundo diferente.
          
    Parabéns por chegar até aqui! Você completou a jornada de Don Quijote no século XXI.
    ''')
    line()

def option(x):
    if x not in [0, 9]:
        while x not in [0, 9]:
            x = int(input(colorText.yellow("Opção inválida! Tente novamente: ")))
        if x == 9:
            # Reiniciar o jogo
            print(colorText.red("Reiniciando o jogo...")) 
            return True
        elif x == 0:
            # Sair do jogo
            print(colorText.red("Saindo do jogo..."))
            exit()
    if x == 9:
        # Reiniciar o jogo
        print(colorText.red("Reiniciando o jogo..."))
        return True
    elif x == 0:
        # Sair do jogo
        print(colorText.red("Saindo do jogo..."))
        exit()


