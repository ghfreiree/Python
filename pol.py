print('Olá, seja bem-vindo ao seu nutricionista digital!!!')
print('Vamos calcular quanto de água você precisa consumir e quantas calorias você precisa consumir diariamente')

peso = int(input('\nQual é o seu peso em kg? '))

qtd_ref = int(input('Quantas refeições você faz por dia? '))

agua = peso*0.035

print(f'\nÁgua: com {peso}kg você precisa consumir {agua:.3f}L de água por dia.')

carb = 5*peso

print(f'Calorias: com {peso}kg, você precisa consumir {carb}g de calorias por dia.')

print(f'\nEm média, você precisa consumir {(agua/16):.3f}L de água por hora.')
print(f'Em média, você precisa consumir {(carb/qtd_ref):.1f}g de calorias por refeição.')