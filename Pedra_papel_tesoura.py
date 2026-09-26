# bibliotecas utilizadas
import random  # serve pra fazer o bot escolher aleatoriamente
import time  # serve pra colocar uma contagem regressiva


def escolha_jogador():
  respostas = ['pedra', 'papel', 'tesoura']  # são as escolhas possiveis para o bot

  while True:
    escolha_aleatoria = random.choice(respostas)

    print('===PEDRA, PAPEL, TESOURA===')
    print('olá gostaria de iniciar uma partida?')
    resposta1 = input('S/N: ')

    if resposta1 in ['S', 's', 'Sim', 'sim', 'y', 'Y']:
      print('escolha mentalmente entre pedra, papel, tesoura')
     #essa parte é o timer pode apagar se quiser
      time.sleep(1)
      print(5)
      time.sleep(1)
      print(4)
      time.sleep(1)
      print(3)  # Corrigido o '3v' para '3'
      time.sleep(1)
      print(2)
      time.sleep(1)
      print(1)
      time.sleep(1)
      #daqui pra baixo não pode apagar
      print('eu escolhi ' + escolha_aleatoria)
    elif resposta1 in ['Nao', 'Não', 'nao', 'não', 'n', 'N']:
      print('por que entrou aqui então?')
      break  # Sai do jogo se disser não no início

    else:
      print('nao reconhecido')

    continuar = input('\nDeseja jogar outra vez? (s/n): ').lower()
    if continuar in ['n', 'nao', 'não']:
      print('Até à próxima!')
      break  # <--- Aqui está o break que "quebra" o ciclo e fecha o programa!
    else:
      print('A reiniciar o jogo...\n')

escolha_jogador()
