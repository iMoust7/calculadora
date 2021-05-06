import time
print('Bem vindo a versão 3.2 da calculadora, se gostar me chame no discord iMoust#0808, e não se esqueça de entrar nesse site https://github.com/iMoust7')
print('_' * 120)

while True:
    print('''
+ adição
- subtração
x multiplicação
vx raiz quadrada
: divisão
:: divisão inteira
% resto da divisão
''')

    print('_' * 120)

    numero1 = float(input('\nEscreva seu primeiro número: ').replace(',', '.'))
    operador = input('\nSeu operador é: ')
    numero2 = float(input('\nEscreva seu segundo número: ').replace(',', '.'))

    print('_' * 120)

    if operador == '+':
        print(f'\n{numero1} + {numero2} = {numero1 + numero2}')

    elif operador == '-':
        print(f'\n{numero1} - {numero2} = {numero1 - numero2}')

    elif operador == 'x':
        print(f'\n{numero1} x {numero2} = {numero1 * numero2}')

    elif operador == 'vx':
        print(f'\n{numero1} vx {numero2} = {numero1 ** numero2}')

    elif operador == ':':
        print(f'\n{numero1} : {numero2} = {numero1 / numero2}')

    elif operador == '::':
        print(f'\n{numero1} :: {numero2} = {numero1 // numero2}')

    elif operador == '%':
        print(f'\n{numero1} % {numero2} = {numero1 % numero2}')

    else:
        print('\n\nVocê colocou o operador errado, tente novamente\n\n\n')

    print('_' * 120)

    pararwhile = input('\nVocê quer continuar a calcular? "S" / "N": ').upper()

    if pararwhile == 'S':
        print('\n\nObrigado por continuar')

    elif pararwhile == 'N':
        print('\nEspero vê-lo novamente\nFechando...')
        time.sleep(5)
        exit()

    else:
        print('\n\nObrigado por continuar')

    print('_' * 120)
