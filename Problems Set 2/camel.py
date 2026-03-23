entrada = input("camelCase: ")

resultado = ""

for cada_letra in entrada:

    if cada_letra.isupper():
        resultado = resultado + "_" + cada_letra.lower()

    else:
        resultado = resultado + cada_letra

print(f"snake_case: {resultado}")
