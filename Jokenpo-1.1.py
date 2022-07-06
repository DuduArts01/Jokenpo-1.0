from random import choice
from time import sleep

#título
print('\033[33m=-=' * 15)
print(' ' * 15, '\033[1;34mJokenpô\033[m')
print('\033[33m=-=\033[m' * 15)

#Computador pensa
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(jokenpo)

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
#Empate
if computador == e:
    print('\033[97mEmpate!\033[m')
    print(f'Você colocou \033[97m{e}\033[m e eu coloquei \033[97m{computador}\033[m')

#condição do usuário vencer:
if computador == 'PEDRA' and e == 'PAPEL':
    print(f'\033[1;4;36mPARABÉNS!!! \033[32mVocê GANHOU! \033[mVocê colocou \033[32m{e}\033[m e eu coloquei \033[31m{computador}.')
elif computador == 'PAPEL' and e == 'TESOURA':
    print(f'\033[1;4;36mPARABÉNS!!! \033[32mVocê GANHOU! \033[mVocê colocou \033[32m{e}\033[m e eu coloquei \033[31m{computador}.')
elif computador == 'TESOURA' and e == 'PEDRA':
    print(f'\033[1;4;36mPARABÉNS!!! \033[32mVocê GANHOU! \033[mVocê colocou \033[32m{e}\033[m e eu coloquei \033[31m{computador}.')

#condição do computador vencer:
if computador == 'PEDRA' and e == 'TESOURA':
    print(f'\033[31mEU GANHEI! \033[33mHAHAHA! \033[mVocê colocou \033[31m{e}\033[m e eu coloquei \033[32m{computador}\033[m')
elif computador == 'PAPEL' and e == 'PEDRA':
    print(f'\033[31mEU GANHEI! \033[33mHAHAHA! \033[mVocê colocou \033[31m{e}\033[m e eu coloquei \033[32m{computador}\033[m')
elif computador == 'TESOURA' and e == 'PAPEL':
    print(f'\033[31mEU GANHEI! \033[33mHAHAHA! \033[mVocê colocou \033[31m{e}\033[m e eu coloquei \033[32m{computador}\033[m')

print('\033[97m-\033[m' * 70)

print('\nBora jogar novamente?')
