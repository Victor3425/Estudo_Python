import re

texto1 = 'aaaaa253G.5155.0911.3462999-Saaaaaa'
texto2 = 'aaaaaaa16.794.464/0028-77aaaaaaaa'
texto3 = '<strong>906550</strong>'
texto4 = '66.970.229/0021-0003.518.732/0102-0040.432.544/0112-6203.518.732/0102-00'


a = re.findall(r'[0-9]{3}[A-Z]{1}.[0-9]{4}.[0-9]{4}.[0-9]{7}-[A-Z]{1}',texto1)

b = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}',texto2)

c = re.findall(r'<strong>(\d+)</strong>',texto3)

d = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}',texto4)

#print(a)
#print(b)
#print(c)
print(d)
