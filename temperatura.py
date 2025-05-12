'''
Sistema que converte temperatura entre Celsius, Fahrenheit e Kelvin
Autor: Gustavo Ganaha Freire (@ghfreiree)
'''

temp1 = input ('Unidade de medida a ser convertida (C, F ou K): ')

temp2 = input('Converter essa unidade de medida para: ')

n1 = float(input(f'Quantos {temp1} serão convertidos: '))

if temp1.upper() == temp2.upper():
    print (n1,temp1, ' é igual a: ', n1, temp2)
elif temp1.upper() == 'C' and temp2.upper() == 'F':
    print (n1, temp1, ' é igual a: ', (n1*(9/5)+32),temp2)
elif temp1.upper() == 'C' and temp2.uppe() == 'K':
    print (n1, temp1, ' é igual a: ', n1+273.15, temp2)
elif temp1.upper() == 'F' and temp2.upper() == 'C':
    print(n1, temp1, ' é igual a: ', (n1-32)*(5/9), temp2)
elif temp1.upper() == 'F' and temp2.upper() == 'K':
    print(n1, temp1, ' é igual a: ', (n1-32*(5/9)+273.15), temp2)
elif temp1.upper() == 'K' and temp2.upper() == 'C':
    print(n1, temp1, ' é igual a: ', n1-273.15, temp2)
elif temp2.upper() == 'K' and temp2.upper() == 'C':
    print(n1, temp1, ' é igual a: ', (n1-273.15)*(9/5)+32, temp2)