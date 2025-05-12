'''
Escreva um programa em Python que simule uma calculadora simples, contendo as quatro operações básicas (+, -, *, / - acrescente mais uma operação).

O programa deve ter:
-Menu de operações
-Realizar o calculo escolhido (dois números)
- Apresentaar o resultado
'''

escolha = input('Qual operação você deseja realizar? (soma, sub, mult, div ou pot): ')

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

match escolha:
    case 'soma': 
        res = n1+n2
        print(f'O resultado é: {res:.1f}')
    case 'sub':
        res = n1-n2
        print(f'O resultado é: {res:.1f}')
    case 'mult': 
        res = n1*n2
        print(f'O resultado é: {res:.1f}')
    case 'div': 
        if n2==0:
            print('Não foi possível realizar a operação (divisão por 0)')
        else: 
            res = n1/n2
            print(f'O resultado é: {res:.1f}')
    case 'pot': 
        res = n1**n2
        print(f'O resultado é: {res:.1f}')