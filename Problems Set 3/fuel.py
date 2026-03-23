while True: 
    try:
        entrada = input ("Fraction: ")

        partes = entrada.split("/")
        x , y = entrada.split("/")

        x = int(x)
        y = int(y)

#se x>y ou x negativo, volta ao início do loop
        if x > y:
            continue

        if x <= 0:
            continue

        porcentagem_num = (x/y)*100

        porcentagem = round(porcentagem_num)

        if porcentagem <= 1:
            print("E")
        elif porcentagem >= 99:
            print("F")
        else:
            print(f"{porcentagem}%")

        break

#se der problema de valor ou dividir por zero, não faz nada e volta o loop
    except ValueError:
        pass

    except ZeroDivisionError:
        pass
        

