"""
Flag (Bandeira) - Marcar um local
None = Nenhum valor
is e is not = é ou nao é(tipo, valor, identidade)
id = Identidade
"""


v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))
print(' ')
condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Nao faça algo')
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)