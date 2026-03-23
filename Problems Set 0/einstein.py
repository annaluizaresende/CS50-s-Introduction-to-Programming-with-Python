#Pedindo para o usuário a massa em kg
m = int(input("Qual a massa em kg? \n"))

#Definindo c como c_quadrado por ser um valor fixo
c = pow(300000000, 2)

#Equação para converter para Joule
Energia = m * c

#Printando
print(f"E = {Energia}")