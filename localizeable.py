import codecs
import pyExcelerator

file = codecs.open('Localizable.strings', 'r', 'utf-8')
string = file.read()
file.close()

string = string.replace('/* No comment provided by engineer. */', '').replace('\n', '')

list = [x.split(' = ') for x in string.split(';')]

workbook = pyExcelerator.Workbook()
ws = workbook.add_sheet('Localizable.strings')

for x in range(len(list)):
    for y in range(len(list[x])):
        if list[x][y]:
            string3 = list[x][y]
            list3 = string3.split('\"')
            ws.write(x,y,list3[1])

workbook.save('localizable.xls')