nome = input('Digite seu nome: ')
idade = input('Digite sua idade')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print('Seu nome invertido é ',  nome[::-1])
    print('Seu nome contem ')
    print('Seu nome contem ',len(nome), ' caracteres')
    print('Seu nome contem ',len(nome), ' letras')
    print('a ultima letra do seu nome é', nome[-1])

    if '' in nome:
        print('Seu nome contém espaço')
    else: 
        print('Seu nome nao contem espaço')
else:
    print('Desculpe, voce deixou campos vazios.')