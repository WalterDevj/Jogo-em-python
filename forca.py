palavra = "python"
letras = []
chances = 4
ganhou = False
Continuar = ""

while True:
    for letra in palavra:
        if letra.lower() in letras:
            print(letra, end=" ")
        else:
            print("-", end=" ")
    print("")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -=1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras:
            ganhou = False

        if chances == 0 or ganhou:
            if ganhou:
                print(f"PARABENS! Você ganhou! a palavra era: {palavra}")
            else:
                print(f"Que pena, você perdeu! A palavra era: {palavra}")
            exit()


