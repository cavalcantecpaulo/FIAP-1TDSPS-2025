
p1 = float(input("Digite o valor do produto 1: "))
print(f"Você digitou o valor: R${p1:.2f}")

p2 = float(input("Digite o valor do produto 2: "))
print(f"Você digitou o valor: R${p2:.2f}")

p3 = float(input("Digite o valor do produto 3: "))
print(f"Você digitou o valor: R${p3:.2f}")

p4 = float(input("Digite o valor do produto 4: "))
print(f"Você digitou o valor: R${p4:.2f}")

p5 = float(input("Digite o valor do produto 5: "))
print(f"Você digitou o valor: R${p5:.2f}")

valor_total = p1+p2+p3+p4+p5
print(f"O valor total é: R${valor_total:.2f}")

valor_pagamento = float(input("Digite o valor do pagamento: "))

if valor_pagamento >= valor_total:
    print(f"Pagamento efetuado: R${valor_pagamento:.2f}")
    if valor_pagamento == valor_total:
        print("Valor de pagamento correto, sem troco a ser devolvido.")
    else:
        troco = valor_pagamento - valor_total
        print(f"O troco a ser devolvido será: R${troco:.2f}")
else:
    print("Não foi possível finalizar a compra, valor do pagamento é menor que o valor de compra!!!")
    print("Sem troco a ser devolvido!!")
