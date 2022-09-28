# Regular Expression
# Jenna Lin
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://www.youtube.com/watch?v=K8L6KVGG-7o&list=WL&index=108&t=322s&ab_channel=CoreySchafer

import re

def find_names(line):
    
    # 1 cap letter + 0 or more lower case + 0 or 1 dot + 0 or 1 space + 1 cap letter + 1 or more lower case
    # + 0 or 1 hyphen + 0 or more cap letter + 0 or more lower case + 0 or more cap letter + 0 or more lower case 
    pattern = re.compile(r'[A-Z][a-z]*\.?\s?[A-Z][a-z]+[A-Z]*[a-z]*\-?[A-Z]*[a-z]*')   
    result = re.findall(pattern, line)
    
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)