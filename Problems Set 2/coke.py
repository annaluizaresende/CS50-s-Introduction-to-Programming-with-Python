falta_pagar = 50

while falta_pagar > 0:
    print(f"Amount Due: {falta_pagar}")

    moeda = int(input("Insert Coin: "))

    if moeda == 25 or moeda == 10 or moeda == 5:
        falta_pagar = falta_pagar - moeda

# Depois que o loop termina, calcula e mostra o troco
if falta_pagar <= 0:
    print(f"Change Owed: {-falta_pagar}")
