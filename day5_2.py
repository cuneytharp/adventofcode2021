# -*- coding: utf-8 -*-
import numpy as np

with open("day5.txt","r") as file: 
    data = file.readlines()

np_arr = np.zeros([1000,1000])
    
data=[x.strip() for x in data]
#counter = 0
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
            
    if abs(x1-x2) == abs(y1-y2):
        diagonal_length = abs(x1-x2)

        if x1<x2 and y1<y2:
            for x in range(1,diagonal_length+1):
                if np_arr[x1+x][y1+x] in np_arr:
                    np_arr[x1+x][y1+x]+=x1
        if x1<x2 and y1>y2:
            for x in range(1,diagonal_length+1):
               if np_arr[x1+x][y1-x] in np_arr:
                   np_arr[x1+x][y1-x]+=x1
        if x1>x2 and y1<y2:
            for x in range(1,diagonal_length+1):
                if np_arr[x1-x][y1+x] in np_arr:
                    np_arr[x1-x][y1+x]+=x1
        if x1>x2 and y1>y2:
            for x in range(1,diagonal_length+1):
                if np_arr[x1-x][y1-x] in np_arr:
                    np_arr[x1-x][y1-x]+=x1
                    
    
{"3-5":0,"4-6":0}           
            
            
print(len(np_arr[np_arr>=2]))  #956593 too high 6133 too low 12315 too low


