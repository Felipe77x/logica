
#Faça um algoritmo que mostre um menu com opções de um cardápio
#de restaurante para a pessoa.

#A pessoa vai escolher o prato desejado digitando o codigo do prato.

#Apos escolher o prato, o algoritmo de mostrar o nome e valor do prato escolhido.


# Entrada 

opcao = int(input("""Código \t Prato \t\t\t Valor
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
    case 2:
       print("Lasanha valor R$ 20,00")
    case 3:
       print("Strogonoff valor R$ 18,00")
    case 4:
       print("Bife acebolado valor R$ 15,00")
    case 5:
       print("Pão com ovo valor R$ 5,00")
 

print(opcao)
