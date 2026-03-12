codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()

numero1 = int(numero1)
valor1 = float(valor1)

numero2 = int(numero2)
valor2 = float(valor2)

total = (numero1 * valor1) + (numero2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")