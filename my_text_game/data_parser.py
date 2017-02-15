import xml.etree.ElementTree as etree

file_default = 'data.xml'

myfile = open('alternative_path', 'r')
alternative_file = myfile.read()


if len(alternative_file) == 0: 
	tree =  etree.parse(file_default)
	root = tree.getroot()
else:
	tree =  etree.parse(alternative_file)
	root = tree.getroot()

