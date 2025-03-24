soma = 0
contador = 0

while True:
    nota = float(input("Digite sua nota: "))
    resposta = input ("Deseja inserir mais uma nota ?? \nDigite 'S' ou 'N' ").upper() 
    if resposta == "N":
        break
    else:
        contador += 1
        soma += nota


# Evita divisão por zero.
if contador == 1:
    soma 

 

