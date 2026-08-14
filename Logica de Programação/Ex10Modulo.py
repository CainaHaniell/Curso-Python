"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número
"""
numero = input('Digite um número inteiro: ')

try: # Captura o erro. O codigo vai executar até chegar no erro e pula para o except
    numero_int = int(numero)

    if numero_int % 2 :
        print(f'o número {numero_int} é impar')
    else:
        print(f'o número {numero_int} é par')

except:
    print('Isso não é um numero.')

