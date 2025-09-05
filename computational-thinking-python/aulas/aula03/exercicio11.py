##11. Ler o tempo gasto em uma viagem (em horas) e a velocidade média (em km/h).
# Calcular a distância percorrida e a quantidade de litros de combustível gasta,
# sabendo que o carro faz 12 km/l.
## Fórmula: distância = tempo * velocidade; litros = distância / 12

horas = float(input("Digite o tempo da viagem em horas: "))
print(f"Você digitou: {horas:.1f} horas.")

velocidade = float(input("Digite a velocidade média (em km/h): "))
print(f"Velocidade: {velocidade:.1f} km/h.")

distancia_total = horas * velocidade
print(f"A distância total do trajeto é: {distancia_total}km.")

litros = distancia_total / 12
print(f"A quantidade de combustível usada no trajeto em litros é: {litros:.1f}l.")


