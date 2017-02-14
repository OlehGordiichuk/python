import xml.etree.ElementTree as etree
#print(dir(etree))
file_for_parse = 'data.xml'
tree =  etree.parse(file_for_parse)
root = tree.getroot()
#print(root.tag)
#print(len(root))

#questlist = []

#for child in root:
#	print(child.text)
#	questlist.append(child.text)
#print(questlist)
