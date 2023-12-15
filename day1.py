# -*- coding: utf-8 -*-

with open("day1.txt","r") as file:
    my_list = file.readlines()
inc_counter= 0 
#my_list =my_list[0:5]
my_list=[int(x.strip()) for x in my_list]

def calculator(list_obj):
    counter = 0
    for index in range(1,len(list_obj)):        
        if list_obj[index]>list_obj[index-1]:
            counter+=1
    return counter

print(calculator(my_list)) # SOLUTION OF FIRST PART

new_list = []
for i in range(len(my_list)):
    if i+2 <len(my_list):
        new_num = my_list[i]+my_list[i+1]+my_list[i+2]
        new_list.append(new_num)

print(calculator(new_list)) #SOLUTION OF SECOND PART