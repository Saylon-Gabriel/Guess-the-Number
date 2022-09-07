import random
import os 
import time
import sys

runGame = True
clear = 'cls' if sys.platform=='windows' else 'clear'

def run(clear):
	os.system(clear)
	erros = 0
	sorteado = random.randrange(0, 100)
	
	try:
		player = int(input('Digite um numero: '))
	except ValueError:
		print('Nao e um numero')
		player = int(input('Digite um numero: '))
		
	while(sorteado != player):
		runGame = False
		os.system(clear)
		if sorteado>player:
			print('Erro, o numero e maior')
		elif sorteado<player:
			print('Erro, numero e menor')
		erros += 1
		
		try:
			player = int(input('Digite um numero: '))
		except ValueError:
			print('Nao e um numero')
			player = int(input('Digite um numero: '))	
			
	print('Voce acertou ' + str(player) + ', em ' + str(erros+1) + ' tentativas')
	time.sleep(2)
	r = input('Jogar novamente? S|N: ').strip().upper()
	if r == 'S':
		runGame = True
	else:
		os.system(clear)
		print('Jogo Encerrado')
		sys.exit()
		
while(runGame == True):
	run(clear)	