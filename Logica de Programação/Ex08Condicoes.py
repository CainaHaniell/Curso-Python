#exercicio de condição entrada e saida
#Se o usuario digitar Entrar EnTrar ou ENTRAR, o sistema tem que aceitar normalmente. 

entrada = input('Digite "ENTRAR", para entrar no sistema e "SAIR" para sair do sistema: ')
letra_maiuscula = entrada.upper()

if letra_maiuscula == "ENTRAR":
    print('Seja bem vindo ao sistema.')
elif letra_maiuscula == "SAIR":
    print('Volte sempre.')
else:
    print('Você digitou errado.')