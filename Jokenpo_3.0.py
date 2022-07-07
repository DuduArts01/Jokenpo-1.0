from random import choice
from time import sleep

novamente = 'S'
vitorias = ["PEDRA-TESOURA", "TESOURA-PAPEL", "PAPEL-PEDRA"]

while novamente == 'S':
    #título
    print('\033[33m=-=' * 15)
    print(' ' * 15, '\033[1;34mJokenpô\033[m')
    print('\033[33m=-=\033[m' * 15)

    #Computador pensa
    jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = choice(jokenpo)
    print(computador)

    #Usuário escolhe
    escolha = input('Escolha: \n[Pedra, Papel, Tesoura]\nQual você prefere? ')
    e = escolha.upper().strip()

    #Fala de jokenpo
    print('Jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('pô!!!')
    sleep(0.5)
    print('\n')
    print('\033[97m-\033[m' * 70)

    resultado = f"{e}-{computador}"

    #Empate
    if computador == e:
        print('\033[97mEmpate!\033[m')
        print(f'Você colocou \033[97m{e}\033[m e eu coloquei \033[97m{computador}\033[m')
    #condição do usuário vencer:
    elif resultado in vitorias:
        print(f'\033[1;4;36mPARABÉNS!!! \033[32mVocê GANHOU! \033[mVocê colocou \033[32m{e}\033[m e eu coloquei \033[31m{computador}.')
    #condição do computador vencer:
    else:
        print(f'\033[31mEU GANHEI! \033[33mHAHAHA! \033[mVocê colocou \033[31m{e}\033[m e eu coloquei \033[32m{computador}\033[m')

    print('\033[97m-\033[m' * 70)
    novamente = input('\nBora jogar novamente? [s/N] ').strip().upper()

# removido alguns declarações if e print(computador)
