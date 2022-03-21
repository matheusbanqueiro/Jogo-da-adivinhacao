print ('==================================')
print ('Bem-vindo ao jogo de advinhação, siga as instruções e descubra o número!')
print ('==================================')
print ('Quantos campeonatos Paulista o corinthians tem?')
print ('******************************************')
print ('Pensou? agora pegue esse número e subtraia a quantidade de campeonatos Brasileiros o corinthians tem!')
print ('******************************************')
print ('Agora pegue esse valor e some com a quantidade de mundiais que o Palmeiras tem!')
print ('******************************************')

numero_correto = 23
tentativas = 0

print ('Antes por favor, defina o nível que você quer:')
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
        tentativas = 20
elif (nivel == 2):
        tentativas = 10
else:
    tentativas = 5


for rodada in range (1, tentativas + 1):
    print ('tentativa {} de {}'.format(rodada, tentativas))

    chute_str = input('digite o resultado:')
    print('Você digitou um número:', chute_str)
    chute = int(chute_str)

    if (chute > 30 or chute < 10):
        print ('uma dica o número está entre 10 e 30')
        continue

    acertou = chute == numero_correto
    maior = chute > numero_correto
    menor = chute < numero_correto

    if (acertou):
        print("Você acertou!")
        break

    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


    print  ('fim de jogo!')
