# 11. Calcular e exibir a área de um retângulo, a partir dos valores da
# base e altura que serão digitados.
##Se a área for maior que 100, exibir a mensagem “Terreno grande”.

base = float(input("Digite a medida da base do retângulo: "))
print("A base do retângulo é: ")

altura = float(input("Digite a medida da altura do retângulo: "))
print("A altura do retângulo é: ")

area_retangulo = base * altura

print(f"A área do retângulo é: {area_retangulo}")
if(area_retangulo>100):
    print("Terreno Grande")