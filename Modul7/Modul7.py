#Nama  : Afrizal Meka M
#NIM   : L200170019 / Kelas A
#Modul : 7



#No.1
import re
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'me[\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#No.2
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'di[\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#No.3
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'di [\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#No.4a
f = open('KEI.html', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'(\w+)</a></td>'
tampil = re.findall(pola,teks)
print(tampil)

pola = r'(\d+)</a></td><td>'
tampil = re.findall(pola,teks)
print(tampil)

#No.4b
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
tampil = re.findall(r'title="([\w+]+)">',teks)
tampil = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
a = []
for i in tampil :
    a.append((i[0], float(i[1])))
print(a)

