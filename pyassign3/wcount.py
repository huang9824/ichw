# -*- coding: utf-8 -*-
"""
@author: Huang Song
@pkuid : 1700091005
"""

import sys
from urllib.request import urlopen

def wcount(line,topn = 10):
    dir = {}
    newline = line.lower()
    word = re.findall(r'[a-z]+',newline)
    for letter in word:
        if letter in dir:
            dir[letter] += 1
        else:
            dir[letter] = 1
    dict = sorted(dir.items(),key=lambda e:e[1],reverse=True)
    dt = {}
    for (m,n) in dict:
        dt.setdefault(m,[]).append(n)
    count = 0
    for key,value in dt.items():
        count += 1
        ss = value[0]
        var = key+"\t\t\t"+str(ss)
        print(var)
        if count == topn:
            pass

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print('Usage:{} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        
    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
         print('{} is not a valid topn int number'.format(sys.argv[2]))
         sys.exit(1)
         
    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
        
        
print(sys,argv)