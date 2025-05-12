''' 
Sistema de compras com carrinho
Autor: Gustavo Ganaha Freire (@ghfreiree)
'''

credito = float(input('Créditos restantes: R$'))
compra = float(input("Valor do produto: R$"))
total = 0
total+=compra
add = input(f'Deseja adicionar mais produtos ao carrinho (R${total:.2f})? s para sim e n para finalizar a compra: ')

if add == 'n' and credito >= total:
    print(f'Pagamento realizado, obrigado pela compra! (Créditos restantes: R${(credito - total):.2f})')
elif total < 0:
    print('Valor inválido')
elif credito == total:
    print('Créditos Zerados. Obrigado pela compra!')
elif credito == 0:
    print('Créditos Zerados.')
elif credito < total:
    print('Créditos insuficientes. Cartão Bloqueado.')
elif credito > 0 and add =='s':
    while add == 's' and credito > total:
        compra = float(input("Valor do produto: R$"))
        total+=compra
        add2 = input(f'Deseja adicionar mais produtos ao carrinho (R${total:.2f})? s para sim e n finalizar a compra: ')
        if add2 == 'n':
            print(f'Pagamento realizado, obrigado pela compra! (Créditos restantes: R${(credito - total):.2f})')
            break
        elif credito == 0:
            print('Créditos Zerados. Obrigado pela compra!')
            break
        elif credito < 0:
            print('Créditos insuficientes. Cartão Bloqueado.')
            break