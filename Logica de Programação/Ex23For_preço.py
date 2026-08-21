preço = [80, 50, 190, 130, 20 , 68]

for preço_produtos in preço:

    if preço_produtos < 100:
        print(f'Produtos  menor que 100:  {preço_produtos}')
    else:
        print(f'Preços barrados: {preço_produtos}')