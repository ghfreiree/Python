''' 
Sistema de compras com carrinho
Autor: Gustavo Ganaha Freire (@ghfreiree)
'''

credito = float(input('Créditos restantes: R$'))
compra = float(input("Valor do produto: R$"))
totalCarrinho = 0
totalCarrinho+=compra
adicionar = input(f'Deseja adicionar mais produtos ao carrinho (R${totalCarrinho:.2f})? Sim para adicionar mais itens ou não para finalizar a compra: ')

if adicionar.upper() == 'NÃO' and credito >= totalCarrinho:
    print(f'Pagamento realizado, obrigado pela compra! (Créditos restantes: R${(credito - totalCarrinho):.2f})')
elif totalCarrinho < 0:
    print('Valor inválido')
elif credito == totalCarrinho:
    print('Créditos Zerados. Obrigado pela compra!')
elif credito == 0:
    print('Créditos Zerados.')
elif credito < totalCarrinho:
    print('Créditos insuficientes. Cartão Bloqueado.')
elif credito > 0 and adicionar.upper() =='SIM':
    while adicionar.upper() == 'SIM' and credito > totalCarrinho:
        compra = float(input("Valor do produto: R$"))
        totalCarrinho+=compra
        adicionar2 = input(f'Deseja adicionar mais produtos ao carrinho (R${totalCarrinho:.2f})? Sim para adicionar mais itens ou não para finalizar a compra: ')
        if adicionar2.upper() == 'NÃO' and credito >= totalCarrinho:
            print(f'Pagamento realizado, obrigado pela compra! (Créditos restantes: R${(credito - totalCarrinho):.2f})')
            break
        elif (credito - totalCarrinho) == 0:
            print('Créditos Zerados.')
            break
        elif (credito - totalCarrinho) < 0:
            print('Créditos insuficientes. Cartão Bloqueado.')
            break