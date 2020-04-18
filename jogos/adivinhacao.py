import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    pontos = 1000

    rodada = 1

    for rodada in range(1, total_tentativas + 1):

        # print("Tentativa {} de {} tentativas".format(rodada, total_tentativas))
        print(f"Tentativa {rodada} de {total_tentativas} tentativas")

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        elif (numero_secreto == chute):
            print(f"Você acertou e fez {pontos} pontos!\n")
            break
        else:
            if (chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto.\n")
            else:
                print("Você errou! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Fim do jogo, o número secreto era {numero_secreto}")


if __name__ == "__main__":
    jogar()
