def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")
    
    palavra_secreta = "maçã".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?: ")
        chute = chute.strip().upper()


        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Você errou! Você tem {6 - erros} tentativas")

        enforcou = erros == 6
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
        print(letras_acertadas)
        print("Você ganhou")
    else:
        print("Você perdeu")
        print(f"A palavra secreta era {palavra_secreta}")

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()