resposta = input("What´s the greeting?\n")

resposta_normalizada = resposta.strip().lower()

if resposta_normalizada.startswith("hello"):
    print("$0")

elif resposta_normalizada.startswith("h"):
    print("$20")

else:
    print("$100")