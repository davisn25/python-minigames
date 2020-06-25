import forca
import adivinhacao

def escolher_jogo():
    print("***************************")
    print("*****Escolha seu jogo!*****")
    print("***************************")

    print("(1)forca  (2)adivinhação")

    jogo = int(input("Qual o jogo?: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()