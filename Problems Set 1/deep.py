
resposta = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")

respostas_normalizadas = resposta.strip().lower()

if respostas_normalizadas in ["42", "forty-two", "forty two", "fortytwo"]:
    print("Yes")

else:
    print("No")

