n = int(input('Digite um número: '))

if (n%2 == 0) or (n%3 == 0) or (n%5 == 0) or (n%7 == 0):
    print('O número não é primo')
else:
    print('O número é primo')