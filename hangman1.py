from random import choice
def pick_random_word():
	f = open('sowpods.txt', 'r')
	line = f.read().split('\n')
	return choice(line)
print(pick_random_word())