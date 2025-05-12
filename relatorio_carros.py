''' 
Sistema que lê o modelo e o consumo de 5 carros, realiza cálculos a partir dos dados informados e gera um relatório geral exibindo o carro de menor utilizando as propriedades da lista.
Autor: Gustavo Ganaha Freire (@ghfreiree)
'''

relatorio = []
validar = 'ok'

for i in range (1, 6, 1):
    carro = input(f'Modelo do carro {i}: ')
    relatorio.append(carro)
    kmL = float(input(f'Km por litro do carro {i}: '))
    validar = 'ok'
    if kmL <= 0:
        print('Erro: Valor inválido')
        validar = 'nOk'
        break
    relatorio.append(kmL)


if validar == 'ok':
    y = 1
    for x in range (0, 10, 2):
        print(f'\nVeículo {y}')
        print(f'Nome: {relatorio[x]}')
        print(f'Km por litro: {relatorio[x+1]}')
        y += 1
    print('\nRelatório Final')
    j = 1
    for z in range (0, 10, 2):
        print(f'{j} - {relatorio[z]}           - {relatorio[z+1]} -   {(1000/(relatorio[z+1])):.2f} - {((1000/(relatorio[z+1]))*6.89):.2f}')
        j+=1

'''O relatorio será impresso em formato de tabela com os respectivos campos:
Modelo do carro, km/L do carro, consumo em litros para 1000 km e custo para 1000 km (considerando a gasolina com preço de R$6.98 reais por litro)
'''

valores = [relatorio[1], relatorio[3], relatorio[5], relatorio[7], relatorio[9]]

menorValor = max(valores)

if menorValor == relatorio[1]:
    print(f'O  menor consumo é do {relatorio[0]}')
elif menorValor == relatorio[3]:
    print(f'O  menor consumo é do {relatorio[2]}')
elif menorValor == relatorio[5]:
    print(f'O  menor consumo é do {relatorio[4]}')
elif menorValor == relatorio[7]:
    print(f'O  menor consumo é do {relatorio[6]}')
elif menorValor == relatorio[9]:
    print(f'O  menor consumo é do {relatorio[8]}')