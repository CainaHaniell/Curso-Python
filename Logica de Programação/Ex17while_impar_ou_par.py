"""
Pedir para o usuario digitar um número e vê se é impa ou par
"""
while True:
    print('\nDigite um número para o sistema verificar se é Impar ou Par ')
    numero = input('Digite um número: ')
    numero_float = float(numero)

    if numero_float %2 ==0:
        print('Esse número é Par')
      
    else:
        print('Esse número é impar')
        
    
    sair = input('Deseja sair? [S]air:').lower().startswith('s')
    if sair == 'sair':
        print('Saindo...')
        break