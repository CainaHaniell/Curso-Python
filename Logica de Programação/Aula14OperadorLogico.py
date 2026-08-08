"""
OPERADORES LÓGICOS
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falsy (valores considerado falsos), a expressao inteira
será avaliada naquele valor.

São considerados falso
0 (zero) 0.0 (float) '' (Strings vazia) False

Também existe o tipo None (Valor que nao existe) que é
usado para representar um não valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

# if True: 
# Digitar E e digitar a senha correta.
senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
   print('Sair')

# Avaliação de curto circuito -> Checa até onde for falso pois a expressao inteira vai ser falso
# print(True and True and True and False)
# print(True and 0 and True)
print(True or False or 0 or 'abc') #Só vai ser false quando os dois forem falso.
print(False or False) 

# Operador Lógico "not"
# Usado para inverter expressões!!
# not True = False
# not False = True
print(not True)
print(not False)

senha = input('Senha: ')

# if senha == '123456':
#     print('Senha correta.')
if not senha:
    print('Voce nao digitou nada')
