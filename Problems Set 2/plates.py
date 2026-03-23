def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Apenas letras e números
    for cada_caractere in s:
        
        if not cada_caractere.isalpha() and not cada_caractere.isdigit():
            return False

    # Ter entre 2 e 6 caracteres
    if len(s) < 2 or len(s) > 6:
        return False

    # Primeiro e segundo caracteres devem ser letras
    if not s[0:2].isalpha():
        return False

    # Números só no final (não pode letra após número) e primeiro número não pode ser 0
    encontrou_numero = False

    for cada_caractere in s:

        if cada_caractere.isdigit():
            if not encontrou_numero and cada_caractere == "0":
                return False
            encontrou_numero = True

        elif cada_caractere.isalpha():
            if encontrou_numero:
                return False

    # Se passou por todas as regras
    return True

main()