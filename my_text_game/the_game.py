# -*- coding: utf-8 -*-
import sys
import data_parser
import random
import math
health = 10
difficulty = 2

while health>0:
	print(data_parser.root[random.randint(0,len(data_parser.root)-1)].text)
	answer = input('Повоюємо? (Y/n) ')

	if answer.lower() == 'y' or answer.lower() == 'yes':
		damage = random.randint( 0, math.ceil(health/difficulty))
		if damage == 0:
			print('везучий Дідько!! Вбив ворога першим Постріло!!м')
		else:
			print('бій коштував вам трохи здоровя! здоровя поменшало на {} одиниць'.format (damage))

		
		health = health - damage

	elif answer.lower() == 'n' or answer.lower() == 'no' :
		damage =  random.randint( 0, math.ceil(health/(difficulty*3)))
		if damage == 0:
                        print('везучий Дідько!! Ти швидко і вчасно бігаєш!')
		else:
                        print('Що ж, втеча коштувала вам трохи здоровя! і його поменшало поменшало на {} одиниць'.format (damage))
		health = health - damage
	else:
		print('хто не відповідає аккуратно і правильно той гру  не грає')
		sys.exit(1)
	
	print('Рівень здоровя:{} одиниць'.format(health))
	print('ОГО!!   НОВИЙ МОНСТР!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
else:
	print('you dead')

print('game over')
print('*************************************************')
