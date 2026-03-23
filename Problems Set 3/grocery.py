itens = {}

while True:

    try:
        ingrediente = input("")

        #Deixando os ingredientes todos em minúsculo
        ingrediente_normalizado = ingrediente.lower()

        #se o ingrediente já foi falado: quantidade de vezes que já foi falado + 1
        if ingrediente_normalizado in itens:
            itens[ingrediente_normalizado] = itens[ingrediente_normalizado] + 1
        
        #se não foi falado ainda, é a quantidade 1
        else:
            itens[ingrediente_normalizado] = 1

    except EOFError:
        break

#ordem alfabetica sorted(x)
for item in sorted(itens):
    quantidade = itens[item]
    print(f"{quantidade} {item.upper()}")