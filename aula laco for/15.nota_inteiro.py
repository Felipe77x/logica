
contador = 0
soma = 0
media = 0

while True:
    nota_inteiro = int(input("Digite suas notas:"))
    
    if nota_inteiro < 0 and nota_inteiro == None:
        print("Programa finalizado")
        break
    soma += nota_inteiro
    contador += 1
    media = soma / contador
    print(f"Sua média foi de {media:.1f}")

    
        
   