resposta = input("What´s the file name?\n")

resposta_normalizada = resposta.strip().lower()

if resposta_normalizada.endswith(".gif"):
    print("image/gif")

elif resposta_normalizada.endswith((".jpg", ".jpeg")):
    print("image/jpeg")

elif resposta_normalizada.endswith(".png"):
    print("image/png")

elif resposta_normalizada.endswith(".pdf"):
    print("application/pdf")

elif resposta_normalizada.endswith(".txt"):
    print("text/plain")

elif resposta_normalizada.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
