"""
Projeto feito para praticar o While com uma condicao
"""
sistema_ativo = True
caixa_saldo = 0
while sistema_ativo:
    caixa = int(input('===== CAIXA =====\n' \
    '1 - Adicionar dinheiro\n' \
    '2 - Retirar dinheiro\n' \
    '3 - Consultar saldo\n' \
    '4 - Sair\n' \
    'Escolha: '))

    if caixa == 1:
      
        deposito = input('Quanto você deseja depositar? ')
        deposito_feito = float(deposito)
        caixa_saldo += deposito_feito
        print('Deposito Concluido\n')

    elif caixa == 2:
        retirar = input('Qunto você deseja retirar? ')
        retirar_saldo = float(retirar)
        
        if retirar_saldo > caixa_saldo or retirar_saldo < 0 :
            print('Você não pode Retirar')
        else:
            print(f'Você retirou {retirar} R$ da sua conta','\n')
            caixa_saldo -= retirar_saldo
    elif caixa == 3:
        print(f'Seu saldo atual é de: {caixa_saldo}','\n')
    elif caixa == 4:
        sistema_ativo = False
        print('Saindo...')