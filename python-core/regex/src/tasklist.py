import re
import os

f =os.popen('tasklist /nh','r')
for eachLine in f:
    #print(eachLine.rstrip())
    print(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',eachLine.rstrip()))
f.close()

