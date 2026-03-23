expressao = input("What's the espression?\n")

partes = expressao.split()
x, y, z = expressao.split()

x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")
#1 casa depois da virgula

elif y == "-":
    print(f"{x - z:.1f}")

elif y == "*":
    print(f"{x * z:.1f}")

elif y == "/":
    print(f"{x / z:.1f}")
