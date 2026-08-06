# if / elif / else
# se / se nao se / se nao

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': #if/elif/else dependem um do outro (IF pode ser usado sozinho se tiver 2 condicao)
    print('Você entrou no sistema')
elif entrada == 'sair': #Se nenhuma das 2 alternativa forem atendida, o else entra. 
    print('Você saiu do sistema')
else:
    print('Voce digitou nenhuma das alternativas')
