# -*- coding: utf-8 -*-
with open("day3.txt","r") as file:
    my_list = file.readlines()

my_list = [x.strip() for x in my_list]


def recurse(my_list,col_index):
    one=0
    zero=0
    for line in my_list:
        if line[col_index]=="1":
            one+=1
        else: 
            zero+=1
    if one>=zero:
        decider = "1"
    else:
        decider = "0"
    my_list= [x for x in my_list if x[col_index] == decider]
    if len(my_list)==1:
        return my_list
    col_index +=1
    return recurse(my_list,col_index)
        
result = ["xx"]
def recurse2(my_list,col_index):
    one=0
    zero=0
    
    for line in my_list:
        if line[col_index]=="1":
            one+=1
        else: 
            zero+=1
    if one>=zero:
        decider = "1"
    else:
        decider = "0"
    my_list= [x for x in my_list if x[col_index] == decider]
    if len(my_list)==1:
        #print("RES BEFORE",result) 
        result =  my_list
        print("RES:",result)
        return
    col_index +=1
    recurse2(my_list,col_index)


recurse2(my_list,0)
print(result) 



