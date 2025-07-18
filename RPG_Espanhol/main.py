from Colors import colorText
from History import session1, session2, session3, sessionLast

print(colorText.lightBlue('-=-' * 34))
print(colorText.blue("<<< RPG - Don Quijote en el siglo XXI >>>".center(100)))
print(colorText.lightBlue('-=-' * 34))
print('''
-> Don Quijote, renascido no século XXI, vê o mundo moderno como 
cheio de "monstros invisíveis". Ele interpreta a realidade com 
sua visão romântica e idealista, e tenta lutar contra injustiças
contemporâneas.
''')

while True:
# Primeira sessão da história
    session1.h()
    print('''
[1] O Castelo das Antenas (Centro de Transmissão)
[2] O Mercado das Almas (Shopping Center)
[3] O Gueto dos Oprimidos (Favela nas Redondezas)
[0] Sair do jogo
''')
    opc1 = int(input(colorText.purple('Escolha uma opção: ')))
    session1.option(opc1)

# Segunda sessão da história
    session2.h()
    print('''
[1] A Arena das Marionetes (Estúdio de Reality Show)
[2] O Santuário Esquecido (Biblioteca Pública Abandonada)
[3] A Torre dos Dragões de Ouro (Prédio de uma Mega-Corporação)
[0] Sair do jogo
''')
    opc2 = int(input(colorText.purple('Escolha uma opção: ')))
    session2.option(opc2)

# Terceira sessão da história
    session3.h()
    print('''
[1] O Livro das Mentiras (Departamento de Censura e Algoritmos)
[2] A Ordem dos Últimos Poetas (Clube Literário Subterrâneo)
[3] O Labirinto das Vozes (Instituto de Neurotecnologia)
[0] Sair do jogo
''')
    opc3 = int(input(colorText.purple('Escolha uma opção: ')))
    session3.option(opc3)

# Sessão final da história
    sessionLast.h()
    print('''
[9] Jogar novamente
[0] Sair do jogo
''')
    opcFinal = int(input(colorText.purple('Escolha uma opção: ')))
    sessionLast.option(opcFinal)
    