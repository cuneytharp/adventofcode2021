# -*- coding: utf-8 -*-
import numpy as np 
with open("day9.txt","r") as file:
    data = file.readlines()

y = len(data)
x = len(data[0])-1
np_arr = np.zeros([x,y])

for row,line in enumerate(data):

    line = [x.strip() for x in line]
    line = [x for x in line if x != ""]

    for  col,char in enumerate(line):
        np_arr[col,row]=int(char)
np_arr = np.transpose(np_arr)

adjacents= []
result_list = []
for i in range(np_arr.shape[0]):
    for j in range(np_arr.shape[1]):
        if i-1 >=0:
            adjacents.append(np_arr[i-1][j])
        if i+1<np_arr.shape[0]:
            adjacents.append(np_arr[i+1][j])
        if j-1 >=0:
            adjacents.append(np_arr[i][j-1])
        if j+1<np_arr.shape[1]:
            adjacents.append(np_arr[i][j+1])
        if np_arr[i][j] <min(adjacents):
            #print("eklendi")
            result_list.append(np_arr[i][j])
        #print(adjacents, np_arr[i][j])
        adjacents=[]
print("RESULT",result_list)  
answer = 0   
for item in result_list:
    answer += item + 1
print(answer)
    
