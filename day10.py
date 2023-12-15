# -*- coding: utf-8 -*-
with open("day10.txt","r") as file:
    data =file.readlines()
data = [x.strip() for x in data]
db = { "(" : ")" ,  "{" : "}", "<" : ">" , "[":"]",")":0,"}":0,"]":0,">":0}
print(db["("])
condition= False
for index,line in enumerate(data[2:3]):
    print("Original",line)
    #while condition == False:
        # line =[x for x in line]
        #line = [x for index_col, x in enumerate(line) if line[index_col+1   ] != db[str(line[index_col])]]

    for index_col, char in enumerate(line):
        if index_col+1<len(line):
            print(index_col)
            if line[index_col +1] ==db[line[index_col]]:
                line=line[:index_col]+line[index_col+2:]
                print(line)
                index_col = 0
        if len(line)==0:
            condition=True
            break
        # if index_col+1<len(line):
        #     if line[index_col+1] == db[line[index_col]]:
        #         print(line)
        #         print(line[index_col:index_col+2],"SİLİNDİ")
        #         line=line[:index_col]+line[index_col+2:]
        #         print(line)
        
            
