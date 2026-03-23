frase = input("Input: ")

for cada_letra in frase:

    if cada_letra not in "AEIOUaeiou":
        print(cada_letra, end = "")

