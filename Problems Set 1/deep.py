
resposta = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")

normalizar = resposta.strip().lower()

if normalizar in ["42", "forty-two", "forty two"]:
    print("Yes")

else:
    print("No")

