# -*- coding: utf-8 -*-
import numpy as np
with open("day5.txt","r") as file: 
    data = file.readlines()

np_arr = np.zeros([1500,1500])
    
data=[x.strip() for x in data]
for line in data: 
    line = line.split(" ")
    x1,y1 = int(line[0].split(",")[0]) , int(line[0].split(",")[1])
    x2,y2 = int(line[2].split(",")[0]) , int(line[2].split(",")[1])
    
    if x1 == x2:
        for point in range(min(y1,y2),max(y1,y2)+1):
            np_arr[(x1)][point] += 1
    if y1 == y2:
        for point in range(min(x1,x2),max(x1,x2)+1):
            np_arr[point][y1] += 1
print(len(np_arr[np_arr>=2])) 


