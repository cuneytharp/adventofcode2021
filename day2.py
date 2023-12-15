# -*- coding: utf-8 -*-
with open("day2.txt","r") as file:
    my_list = file.readlines()

my_list = [x.strip() for x in my_list]

horizon = 0 
depth = 0 
aim = 0 

for line in my_list:
    command, num = line.split(" ")
    num=int(num)
    print(command , num)
    if command=="forward":
        horizon += num
        depth += aim*num
    if command=="up":
        #depth -=num
        aim -= num
    if command=="down":
        #depth += num
        aim += num
    print("AIM",aim, "DEPTH",depth,"HORIZON",horizon)
print(horizon,depth)
print(horizon*depth)
        
    

