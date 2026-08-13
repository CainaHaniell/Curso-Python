"""
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar execultar
"""

numero_str = input('Vou dobrar o numero que você digitar: ')

try: # Captura o erro. O codigo vai executar até chegar no erro e pula para o except
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero.')
 
# print(numero_str.isdigit()) # Ve se o usuario digitou apenas numeros ou pontos
# if numero_str.isdigit():
#   
# else: