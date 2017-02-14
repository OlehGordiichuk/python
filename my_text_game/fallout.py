import sys

#command = sys.argv[1]
#print(command)
if len(sys.argv)>2 or len(sys.argv)<2  or sys.argv[1] == '--help':
        print ('''usage: fallout [-arg]
arguments:
  -arg: --help            show this help message and exit
        --import_quests   launch quest imorter
        --start           launch the game''')
        sys.exit(1)

elif sys.argv[1] == '--import_quests' :
#	import data_parser #get_quests
#	print('import get_quests')
	print('no works yet')
#	print(len(data_parser.root))
elif sys.argv[1] == '--start':
	import the_game
#	print('import the_game')
else:
	print('unknown Shit')
	sys.exit(1)

input('just for wait')
