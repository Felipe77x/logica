

def produto(pedir_produto):

    
 
    if pedir_produto < 100: 
        resultado = pedir_produto * 1.10
  
    else: 
        resultado = pedir_produto * 1.20
    return resultado



pedir_produto = float(input("Coloque o pedido:"))
preco_produto = produto(pedir_produto)
print(f"Preço final: {preco_produto}")




def produto_desconto(pedir_produto):

    
 
    if pedir_produto < 100: 
        resultado = pedir_produto * 0.9
  
    else: 
        resultado = pedir_produto * 0.8
    return resultado



pedir_produtos = float(input("Coloque o pedido:"))
preco_produtos = produto_desconto(pedir_produto)
print(f"Preço final: {preco_produtos}")

