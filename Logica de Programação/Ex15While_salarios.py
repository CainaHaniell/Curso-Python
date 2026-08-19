print("+" + "-" * 30 + "+")
print("|  Bem vindo a receita federal" + " " * 1 + "|")
print("+" + "-" * 30 + "+")


salario = 0

while salario <= 4500: 
    salario_atual = (input('Digite seu salário: '))
   
    try:
       salario_float = float(salario_atual)
       salario += salario_float
       print(f'Seu salário atual é de: {salario} \n')

    except:
        print('Erro, isso nao é salário')

print(f'Salario barrado pois passou de limite.\nSeu salario atual: {salario:.2f}')