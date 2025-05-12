''' 
Cálculo de calorias consumidas em refeições
Este sistema exibe o total de calorias consumidas em várias refeições e a média de calorias por refeição utilizando listas
Autor: Gustavo Ganaha Freire (@ghfreiree)
'''

resposta = ''
calorias = []

while resposta.upper() != 'NÃO':
    caloria_refeicao = int(input('Quantas calorias você consumiu nessa refeição? '))
    calorias.append(caloria_refeicao)
    resposta = input('Você teve mais uma refeição? ')

print(f'Você consumiu {calorias} calorias')

total = 0

for caloria_refeicao in calorias:
    total += caloria_refeicao
print(f'Total de calorias consumidas: {total}')
media = total/len(calorias)
print(f'Média de calorias consumidas por refeição: {media}')
