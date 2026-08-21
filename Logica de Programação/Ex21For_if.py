produtos_loja = ["Mouse", "Teclado", "Monitor", "Notebook"]

for produtos in produtos_loja:
    
    if len(produtos) > 6:
        print(f'Produtos que contem 6 letras {produtos}','')
    else:
        print(f'Produto que contem menos de 7 Letras {produtos}')