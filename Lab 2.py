import re

ipPattern = re.compile(r'((?:[0-9]{1,3}\.){3}[0-9]{1,3})')
with open("access.log",'r',encoding='utf-8') as f:
    s = f.read()
iplist = ipPattern.findall(s)
subnetDict ={}
for i in iplist:
    t = re.match(r'((?:[0-9]{1,3}\.){2}[0-9]{1,3})',i).group(0)
    if subnetDict.get(t) == None:
        subnetDict[t] = set([i])
    else:
        subnetDict[t].add(i)

for i in subnetDict:
    print(i)
    print('  ',subnetDict[i])
    print('\n')
