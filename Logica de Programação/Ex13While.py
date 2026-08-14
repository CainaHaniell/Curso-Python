"""
Iterando strings com while
"""
# 012345678910
nome = 'Pedro Barbeiro'
tamanho_string = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
