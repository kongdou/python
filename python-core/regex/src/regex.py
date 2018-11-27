import re

# match
m = re.match('foo', 'foo')
if m is not None: print(m.group(0)) # 返回foo

m = re.match('foo', 'food')
if m is not None: print(m.group(0)) # 返回foo

m = re.match('foo', 'dfoo')
if m is not None: print(m.group(0)) # 无返回结果

#search
m = re.search('food', 'myfood')# 返回food
if m is not None: print(m.group(0))

# 匹配多个字符串
bt = 'bat|bet|bit'
m = re.match(bt,'batd')
if m is not None: print(m.group(0)) # 返回bat

# 匹配单个字符
bt = '.end'
m = re.match(bt,'oend')
if m is not None: print(m.group(0)) # 返回oend

# 字符集
bt = '[cr][23][dc][59]'
m = re.match(bt,'c2d5')
if m is not None: print(m.group(0)) # 返回c2d5

# 重复、特殊字符
patt = '\w+@(\w+\.)?\w+\.com'
m=re.match(patt,'henuxiaojie@126.com')
if m is not None: print(m.group(0)) # henuxiaojie@126.com
m=re.match(patt,'henuxiaojie@www.126.com')
if m is not None: print(m.group(0)) # henuxiaojie@www.126.com
m=re.match(patt,'henuxiaojie@www.xxx.126.com')
if m is not None: print(m.group(0)) # 不返回结果

patt = '\w+@(\w+\.)*\w+\.com'
m=re.match(patt,'henuxiaojie@www.xxx.126.com')
if m is not None: print(m.group(0)) # henuxiaojie@www.xxx.126.com

# 分组(..)
g = '(\w\w\w)-(\d\d\d)'
m = re.match(g,'abc-123')
if m is not None: print(m.group(0) +':'+m.group(1)+','+m.group(2)) # 返回结果abc-123:abc,123

# 子组()
g='(ab)'
m = re.match(g,'ab')
if m is not None: print(m.groups()) # ('ab',)
if m is not None: print(m.group()+","+m.group(1))#ab,ab

# 子组()
g='(a(b))'
m = re.match(g,'ab')
if m is not None: print(m.groups())

# 起始
s = "^The"
m=re.search(s,"The end.")
if m is not None: print(m.group())#The

m=re.search(s,"End The")
if m is not None: print(m.group())#无结果

# 边界
m = re.search(r'\bthe','bite the dog')
if m is not None: print(m.group())#the

m = re.search(r'\bthe','bitethe dog')
if m is not None: print(m.group())#无结果

# 无边界
m = re.search(r'\Bthe','bitethe dog')
if m is not None: print(m.group())#the

# findall 与match不同的是返回一个列表，如果没有则返回空列表
m=re.findall('all','all')
if m is not None: print(m)#返回['all']

m=re.findall('all','all---all')
if m is not None: print(m)#返回['all', 'all']

s='this and that'
m=re.findall(r'(th\w+) and (th\w+)',s,re.I)
if m is not None: print(m)#[('this', 'that')]

# findter
s='this and that'
m=re.finditer(r'(th\w+) and (th\w+)',s)
for i in m:
    print(i.group())  # this and that


# sub
m = re.sub('X','Mr.Smith','attn:X\n\n Dear X,\n')
print(m)
m = re.subn('X','Mr.Smith','attn:X\n\n Dear X,\n')
print(m)


# ?: 对部分正则表达式分组，但不保存该分组用于后续的检索和应用
m = re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
if m is not None: print(m) # 结果 ['google.com', 'google.com', 'google.com']

# ?P<>
m = re.search(r'\((\d{3})\) (\d{3})-(\d{4})','(800) 555-1212')
print(m.group()) # (800) 555-1212
print(m.groupdict()) # {}
print(m.group(1)) # 800
print(m.group(2)) # 555
print(m.group(3)) # 1212

m = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212')
print(m.group()) # (800) 555-1212
print(m.groupdict()) # {'areacode': '800', 'prefix': '555'}
print(m.group(1)) # 800
print(m.group(2)) # 555
#print(m.group(3)) # 不存在报错

# ?= 前视匹配
m=re.findall(r'\w+(?= van Rossum)',
             '''
             Guido van Rossum
             Tim Peters
             Dee van Rossum
             ''')
print(m) # 结果['Guido', 'Dee']

# ?! 负先前，查找不是zhangsan、lisi的邮箱
m=re.findall(r'(?m)^\s+(?!zhangsan|lisi)(\w+)',
             '''
                zhangsan@xxx.com
                lisi@xxx.com
                deepsky@xxx.com
             ''')
print(m)

m=['%s@aw.com' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!zhangsan|lisi)(\w+)',
                                      '''
                                      zhangsan@xxx.com
                                      lisi@xxx.com
                                      deepsky@xxx.com  
                                   ''')]
print(m) #结果['deepsky@aw.com']