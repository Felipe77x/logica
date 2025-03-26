contador_par = 0
contador_impar = 0
soma = 0
while True:
    
    numero = int(input("Digite apenas numeros inteiros."))
    numero_ok += 1
   

    if numero < 0:
        print("Código finalizado.")
        break
  

    par = numero % 2 == 0
    contador_par += 1
    
    soma += par
    media = contador_impar / soma

    impar = numero % 2 == 1
    contador_impar += 1

    media_geral = numero / numero_ok


    print(contador_par)
    print(contador_par)
    print(media)
    print(media_geral)