i=int(input('Digite o valor inicial: '))
f=int(input('Digite o valor final: '))

if i<f:
    while i<=f:
        if i%2 == 0:
            print(f'i: {i}')
        i+=1
elif i>=f:
    while i>f:
        if f%2 == 1:
            print(f'f:{f}')
        f+=1
elif i==f:
    print(i)