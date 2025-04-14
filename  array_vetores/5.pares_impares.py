 lista_impar_par = []

def impar_par (lista_impar_par,numero,contador_par, contador_impar):

    contador_par = 0
    contador_impar = 0
   
    numero = int(input("Digite seus números:"))
    lista_impar_par.append(numero)
    if numero % 2 == 0:
        contador_par += 1  
    else:
        contador_impar += 1 
    

    print(f"A quantidade de números pares é: {contador_par}")
    print(f"A quantidade de números ímpares é: {contador_impar}")
    
