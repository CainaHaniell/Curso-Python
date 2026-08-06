
# # 6 - EXERCICIO CONVERTER HORAS EM MIN, E MIN EM HORAS
# # E CONVERTER HORAS PARA DIA

# # Exemplo, todos os dias vou estudar x horas.

hora_Min = float(input('Digite quantas horas quer converter em min: '))

calculo_hora = hora_Min * 60

print(f'{hora_Min} hora em minutos é: {calculo_hora:.0f} minutos')

hora_Min = float(input('\nDigite quantas horas quer converter em dias: '))

calculo_dia = (hora_Min / 24) 

print(f'{hora_Min} horas convertendo em dias fica: {calculo_dia:.0f} dias')


# USUARIO VAI DIGITAR QUANTAS HORAS DESTINADA VAI ESTUDAR E O SISTEMA VAI
# CALCULAR QUANTO TEMPO ELE VAI TERMINAR O CURSO

import math 

print('\nCalculadora de Dias para Concluir o Curso')
horas_curso = float(input('Quantas horas o curso tem: '))
horas_estudos = float(input('Quantas horas por dia você vai estudar: \n'))

calculo_horas_por_dia = math.ceil(horas_curso / horas_estudos)

print(f'Você vai ter {calculo_horas_por_dia:.0f} dias para terminar o curso')
