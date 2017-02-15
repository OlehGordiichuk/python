import sys

def help_print():
	print ('''usage: fallout [-arg]
arguments:
  -arg: --help		show this help message and exit
        --import	launch quest imorter
        --start		launch the game''')
	sys.exit(1)


if len(sys.argv)>2 or len(sys.argv)<2  or sys.argv[1] == '--help':
    help_print()

elif sys.argv[1] == '--import' :
	import get_quests
	help_print()

elif sys.argv[1] == '--start':
	import the_game

else:
	print('unknown Shit')
	sys.exit(1)

input('just for wait')
