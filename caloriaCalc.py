
resposta = ''
calorias = []

while resposta.upper() != 'NÃO':
    caloria = int(input('Quantas calorias você consumiu nessa refeição? '))
    calorias.append(caloria)
    resposta = input('Você teve mais uma refeição? ')

print(f'Você consumiu {calorias} calorias')

total = 0

for caloria in calorias:
    total += caloria
print(f'Total de calorias consumidas: {total}')
media = total/len(calorias)
print(f'Média de calorias consumidas por refeição: {media}')
