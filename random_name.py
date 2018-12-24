import random

name = ['123', '456', '789']
while name:
	press = input('Input enter: ')
	winner = random.choice(name)
	print('winner is: ', winner)
	print('-------------------------------------')
	name.remove(winner)
	print('Maybe you are winner: ', name)
	print('/////////////////////////////////////')