"""
Imprrimir só a letra que nao se repete
"""

palavra = input('Digite uma palavra: ')

for letra in palavra:

    if palavra.count(letra) == 1:
        print(f'a letra: {(letra)} 1 vez') 