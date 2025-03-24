total = 0

while True:
    opcao = int(input(f"""Código \t Prato \t\t\t Valor
   1 \t Picanha \t\t  R$ 25,00
   2 \t Lasanha \t\t R$ 20,00
   3 \t Strogonoff \t\t R$ 18,00
    4 \t Bife acebolado \t R$ 15,00
   5 \t Pão com ovo \t\t R$ 5,00 
                  
    Digite a opção desejada:                  
                  """))

    match opcao:
        case 1:
            print("Picanha valor R$ 25,00")
            total += opcao
        case 2:
            print("Lasanha valor R$ 20,00")
            total += opcao
        case 3:
            print("Strogonoff valor R$ 18,00")
            total += "valor"
        case 4:
            print("Bife acebolado valor R$ 15,00")
            total += opcao
        case 5:
            print("Pão com ovo valor R$ 5,00")
            total += opcao
  

            print("Deseja escolher o prato novamente ? ")
            break