"""
Exercicio While
Usuario vai digitar 2 numero e um sinal de operação
O sistema vai entregar o numero, vê se ele é par, ou impa e continuar
até que o usuario digite a palavra 'sair'
"""



while True:
    num1 = float(input('Digite um número que queira multiplicar: '))
    num2 = float(input('Digite outro número que queira multiplicar: '))
    operacao = input('Digite a operação que deseja: [+ - * /] ')

    if operacao == '+':
        soma = num1 + num2
        print('\nA soma dos número é: ', soma)
        if soma %2 ==0:
            print('Esse número é par')
        else: 
            print('Esse número é impar')
            
    elif operacao == '-':
        soma = num1 - num2
        print('\nA subtração dos número é: ', soma)
        if soma %2 ==0:
            print('Esse número é par')
        else: 
            print('Esse número é impar')

    elif operacao == '*':
        soma = num1 * num2
        print('\nA multiplicação dos número é: ', soma)
        if soma %2 ==0:
            print('Esse número é par')
        else: 
            print('Esse número é impar')

    elif operacao == '/':
        soma = num1 / num2
        print('\nA divisao dos número é: ', soma)
        if soma %2 ==0:
            print('Esse número é par')
        else: 
            print('Esse número é impar')

    sair = input('Quer sair [S/N]').lower()

    if sair == 's':
        print('Você saiu do programa')
        break