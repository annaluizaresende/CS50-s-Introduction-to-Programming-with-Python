#Definindo a função principal que solicita o input e que usa a função emoji
def main():
    frase = emoji(input("Frase: \n"))
    print(frase)

#Definindo a função emoji que vai trocar os caracteres por emojis
def emoji(e):
    e = (e.replace(":)", "🙂"))
    e = (e.replace(":(", "🙁"))
    return e

#Chamando a função
main()