lista_numero = []
quantidades_numero = 6


def pares_impares(lista):
    pares = 0
    impares = 0 

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
print("=Solicitando numero")
    
