entradas = input().split()

distancia = int(entradas[0])
diametro1 = int(entradas[1])
diametro2 = int(entradas[2])

print(f'{distancia / (diametro1+diametro2):.2f}')
