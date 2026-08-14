contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 20:
        print(f'Não vou mostrar o {contador}')
        continue

    if contador == 10:
        break
    print(contador)
print('acabou')

print('')