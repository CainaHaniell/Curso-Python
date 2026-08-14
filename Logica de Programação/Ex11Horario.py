"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. EX.:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""

hora = int(input('Digite a hora: '))

if hora >= 0 and hora <=11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
else:
    print('Boa noite')