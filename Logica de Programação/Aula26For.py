"""
for -> para cada
numero -> Variavel temporaria 

"""
numeros = [0,2,4,1,7,10,22,14,157,13,13,9,5,3,12]
# For -> para
for numero in numeros:
    #para cada numero dentro de numeros, faça if...
    if numero %2 == 0:
        print(f'{numero} é par')
        continue
    else:
        print(f'{numero} é impar')

print('')

pedras = ('Rubi', 'Diamante', 'Quartzo', 'Safira', 'Turmalina', 'Esmeralda')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)