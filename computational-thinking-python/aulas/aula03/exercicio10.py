##10. Ler o salário de um funcionário e aplicar um aumento de
##15%. Exibir o salário atualizado.

salario = float(input("Digite o salário do funcionário: "))
print(f"Você digitou: R${salario}")
print("Após uma verificação, houve um aumento de 15% no salário do funcionário.")

novo_salario = (salario * 15)/100 + salario

print(f"O novo salário do funcionário é: R${novo_salario}")