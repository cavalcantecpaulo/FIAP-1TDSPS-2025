## 12. Entrar via teclado com três valores distintos.
# Exibir o maior deles.

print("Cálcular maior valor")

a = int(input("Digite o primeiro valor: "))
print(f"Valor digitado: {a}")

b = int(input("Digite o segundo valor: "))
print(f"Valor digitado: {b}")

c = int(input("Digite o terceiro valor: "))
print(f"Valor digitado: {c}")

if (a>b):
    if(a>c):
        print(f"O maior valor digitado é o: {a}")
    if(c>a):
        print(f"O maior valor digitado é o: {c}")
elif (b>a):
    if (b > c):
        print(f"O maior valor digitado é o: {b}")
    if (c > b):
        print(f"O maior valor digitado é o: {c}")
elif (c>a):
    if (c > b):
        print(f"O maior valor digitado é o: {c}")
    if (b > c):
        print(f"O maior valor digitado é o: {b}")
else:
    print(f"Os valores digitados são iguais. Maior valor: {a}")