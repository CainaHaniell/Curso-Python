"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs: a funcao len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:]) # vai do indice 4 até o fim
print(len(variavel[0:3])) #caracteres do indice 0 até o indice 3
print(len(variavel)) # caractere total da frase
print(len(variavel[::-1])) # caractere total da frase