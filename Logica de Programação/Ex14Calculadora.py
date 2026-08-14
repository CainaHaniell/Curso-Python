"""
    Calculadora com while
"""
while True: 
    numero1 = input('Digite um número: ')
    numero2 = input('Digite um segundo número: ')
    operador = input('Qual operação [+ - * /]: ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero1)
        num2_float = float (numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um (1) operador.')
        continue

 

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        
        print(num1_float + num2_float)
    elif operador == '-':
         print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
         print(num1_float * num2_float)
    else:
        print('Nunca deve chegar aqui.')

    sair = input('Quer sair [s]im: ').lower().startswith('s')
    
    if sair is True:
        break