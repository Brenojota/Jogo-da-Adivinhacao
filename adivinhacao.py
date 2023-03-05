import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

    #GERANDO NUMERO (0.0 A 1.0)
numero_secreto = random.randrange(1 , 101)
tentativas = 0
pontuacao = 1000

print("Qual nível de dificuldade?")
print(" (1) Fácil  (2) Médio  (3) Díficil")

nivel = int(input("Defina o nível do jogo:  \n"))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
elif(nivel == 3):
    tentativas = 5
else:
    print("Você digitou um nível INVÁLIDO!")
    tentativas = 0

for rodadas in range(1, tentativas + 1):
    print("RODADA: {} DE {} ".format(rodadas, tentativas))
    chute = input("Digite um numero entre 1 e 100: ")
    print("Você digitou: ",chute)
    chute = int(chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100! \n")
        continue

    # teste booleano
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou! \n")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi Maior que o número secreto \n")
            pontuacao = pontuacao - (chute - numero_secreto)
        else:
            print("Você errou! O seu chute foi MENOR que o número secreto \n")
            pontuacao = pontuacao - (numero_secreto - chute)


print("Fim de jogo")
print("O número secreto é: ",numero_secreto)
print("Você fez {} pontos ".format(pontuacao))