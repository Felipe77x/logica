

def massa_corporal(altura,peso):


    resultado = (peso/ altura ** 2)
    return resultado

altura = float(input("Qual a sua altura:"))
peso = float(input("Qual o seu peso:"))

resultado_media = massa_corporal(altura, peso)

print(f"O seu IMC é: {resultado_media:.2f}")


def imc():
    if resultado_media < 18.5:
        print("Abaixo do peso")
    elif resultado_media == 18.5 and 24.9:
        print("Peso normal")
    elif resultado_media == 30 and 34.9:
        print("Obesidad grau 1")
    elif resultado_media == 35 and 39.9:
        print("Obesidade grau 2")
    elif resultado_media > 40:
        print("Obesidade grau 3")

resultado = massa_corporal(imc(peso,altura))
print(resultado)