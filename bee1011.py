codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()
raio = float(input())

pi = 3.14159
volume = (4/3) * pi * (raio ** 3)

print(f"VOLUME = {volume:.3f}")