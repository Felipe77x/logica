
def tabuada(tabuada_variavel,  tabuada_resultado):
     
    for i in range(1, 11):
    
        tabuada_resultado = tabuada_variavel * i

        print(f"A tabuada {i} x {tabuada_variavel} = {tabuada_resultado}")
tabuada_variavel = int(input("Digite o numero da tabuada:"))
(tabuada(tabuada_variavel))