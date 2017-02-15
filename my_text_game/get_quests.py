file_path =  input('Уведіть назву фалу (data.xml)')

myfile = open('alternative_path', 'w')
myfile.write(file_path)
myfile.close()

print('Файл {} з квестами додано'.format (file_path))
print('*******************************************')
