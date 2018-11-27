import re

data = 'Tue Nov 27 18:33:20 2018::buryh@dzyanstjm.net::6988555747143623259-5-9'
patt='^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'

m = re.match(patt,data)
print(m.group()) #Tue
print(m.group(1)) #Tue

m = re.match('^(\w{3})',data)
if m is not None: print(m.group()) #Tue
if m is not None: print(m.group(1)) #Tue

patt = '^(\w){3}'
m=re.match(patt,data)
if m is not None: print(m.group()) #Tue
if m is not None: print(m.group(1)) #e

patt = '\d+-\d+-\d+'
m=re.search(patt,data)
print(m.group())

patt = '.+\d+-\d+-\d+'
m=re.match(patt,data)
print(m.group())

patt = '.+(\d+-\d+-\d+)'
m=re.match(patt,data)
if m : print(m.group(1))#9-5-9

# 非贪婪模式
patt = '.+?(\d+-\d+-\d+)'
m=re.match(patt,data)
if m : print(m.group(1))#6988555747143623259-5-9


