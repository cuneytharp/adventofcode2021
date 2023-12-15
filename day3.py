# -*- coding: utf-8 -*-
with open("day3.txt","r") as file:
    my_list = file.readlines()

my_list = [x.strip() for x in my_list]
col = len(my_list[0])
my_dict = {f"{x}":{"0":0,"1":0} for x in range(col)}


for line in my_list:
    #print(line)
    temp_list = [int(x) for x in line]
    for col,char in enumerate(temp_list):
        my_dict[f"{col}"][f"{char}"] +=1
print(my_dict,"\n")

max_list = ""
min_list = ""
for i in my_dict.keys():
    
    if my_dict[i]["0"]>my_dict[i]["1"]:
        max_list+="0"
        min_list+="1"
    else:
        max_list+="1"
        min_list+="0"
print(max_list) 1491
print(min_list) 2604
        
        
    
    
 





