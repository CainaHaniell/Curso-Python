print('=' * 10, 'BOLETIM', '=' * 10)

nome = 'Pedro'
idade = 19
rg = '123.123'
idade = 19

print('Nome: ', nome)
print('Idade: ', idade)
print('Rg: ', rg)

print('\nNota do aluno')
nota1 = 7.5
nota2 = 6.5
nota3 = 8.0

media = (nota1 + nota2 + nota3) / 3

print(f'Média: {media:.1f}')

aprovado = media >= 7

print('\nAprovado: ', aprovado)
print('Ano de nascimento: ', 2026 - idade, '\n')

print('Tipo de nome: ', type(nome))
print('Tipo de idade: ', type(idade))
print('Tipo de rg: ', type(rg))
print('Tipo de media: ', type(media))
print('Tipo de aprovado: ', type(aprovado))
