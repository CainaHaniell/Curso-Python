texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
print('')
"""
For + Range
range -> range(start, stop, step (quantos em quantos número quero pular))
"""
numeros = range(1, 10)
for numero in numeros:
    print(numero)
