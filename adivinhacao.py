import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    secret_number= random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    score = 1000

    print("Qual é o nível de dificuldade que tu queres?:")
    print("(1)Fácil  (2)Normal   (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in  range (1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == secret_number
        maior   = chute > secret_number
        menor   = chute < secret_number

        if(acertou):
            print(f"Você acertou e fez {score} pontos")
            break
        else:
            if(maior):
                print("Tente outro número abaixo desse.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {secret_number}. Você fez {score}")
            elif(menor):
                print("Tente outro número acima desse.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {secret_number}. Você fez {score}")

        lost_points = abs(secret_number - chute)
        score = score - lost_points

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()