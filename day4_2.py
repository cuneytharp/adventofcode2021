# -*- coding: utf-8 -*-
import numpy as np
with open("day4.txt","r") as file:
    data = file.readlines()
data =[x.strip() for x in data]

"""
burası verilerden oyunları çıkarıyor ve de numpy array ekliyor
"""
guess_num = [int(x) for x in data[0].strip().split(",")]
game_counter = 1 
game_list = [] 
master_dict = {}

for x in range(2,len(data)):
    if data[x] != "":
        numbers = [int(x) for x in data[x].split(" ") if x != ""]
        #print(numbers)
        game_list.append(numbers)

    if data[x] =="" or x==len(data)-1:
        master_dict.update({game_counter:{"game":game_list,"arr":np.zeros([5,5]),"win_count":0}})
        game_list =[]
        game_counter +=1
######

#lacine iki soru var. 1 game_num in master_dict.keys() diyince olmadı
# bir de bunu fonksiyonsuz yapmak istesem nasıl durdururdum. 

def calculator(guess_num,master_dict):
    win_count = 1
    final_num = 0 
    for num in guess_num:
        for game_num in master_dict.keys():
            #print(game_num)
            for x in range(5):
                if num in master_dict[game_num]["game"][x]:
                    pos = master_dict[game_num]["game"][x].index(num)
                    master_dict[game_num]["arr"][x][pos]=1
                if master_dict[game_num]["arr"][:,x].sum()==5 or master_dict[game_num]["arr"][x,:].sum()==5:
                    if master_dict[game_num]["win_count"]==0:
                        #print("counter 0")
                        master_dict[game_num]["win_count"]=win_count
                        win_count += 1
                    if final_num==0 and win_count==101:
                        final_num = num 
                        print("Final",final_num)                
                        return final_num
                    
                    

final_num = calculator(guess_num, master_dict)
#print(master_dict)
final_dict = {}
for key in master_dict.keys():
    final_dict.update({key:master_dict[key]["win_count"]})
#print(sorted(final_dict.values()))
keymax = max(zip(final_dict.values(), final_dict.keys()))[1]
print(keymax)
new_array = master_dict[keymax]["arr"]
ones = new_array ==1
zeroes = new_array==0
new_array[ones]=0
new_array[zeroes]=1
game_array = np.array(master_dict[keymax]["game"])
print(game_array)
print(new_array)
print((new_array*game_array).sum()*final_num)




# # -*- coding: utf-8 -*-
# import numpy as np
# with open("day4.txt","r") as file:
#     data = file.readlines()
# data =[x.strip() for x in data]

# """
# burası verilerden oyunları çıkarıyor ve de numpy array ekliyor
# """
# guess_num = [int(x) for x in data[0].strip().split(",")]
# game_counter = 1 
# game_list = [] 
# master_dict = {}

# for x in range(2,len(data)):
#     if data[x] != "" and x!=len(data)-1:
#         numbers = [int(x) for x in data[x].split(" ") if x != ""]
#         #print(numbers)
#         game_list.append(numbers)

#     if data[x] =="" or x==len(data)-1:
#         master_dict.update({game_counter:{"game":game_list,"arr":np.zeros([5,5]),"win_count":0}})
#         game_list =[]
#         game_counter +=1
        
# ######

# #lacine iki soru var. 1 game_num in master_dict.keys() diyince olmadı
# # bir de bunu fonksiyonsuz yapmak istesem nasıl durdururdum. 

# def calculator(guess_num,master_dict):
#     win_count = 1
#     for num in guess_num:
#         for game_num in master_dict.keys():
#             #print(game_num)
#             for x in range(5):
#                 if num in master_dict[game_num]["game"][x] and master_dict[game_num]["win_count"]==0:
#                     pos = master_dict[game_num]["game"][x].index(num)
#                     master_dict[game_num]["arr"][x][pos]=1
#                 if master_dict[game_num]["arr"][:,x].sum()==5 or master_dict[game_num]["arr"][x,:].sum()==5:
#                     if master_dict[game_num]["win_count"]==0:
#                         master_dict[game_num]["win_count"]=win_count
#                         win_count +=1
#                     # new_array = master_dict[game_num]["arr"]
#                     # ones = new_array ==1
#                     # zeroes = new_array==0
#                     # new_array[ones]=0
#                     # new_array[zeroes]=1
#                     #game_array = np.array(master_dict[game_num]["game"])
#     return master_dict
                    
                    
# calculator(guess_num, master_dict)
# final_dict = {}
# for key in master_dict.keys():
#     final_dict.update({key:master_dict[key]["win_count"]})
# print(final_dict)
# # keymax = max(zip(final_dict.values(), final_dict.keys()))[1]
# # print(keymax)
# # new_array = master_dict[keymax]["arr"]
# # ones = new_array ==1
# # zeroes = new_array==0
# # new_array[ones]=0
# # new_array[zeroes]=1
# # game_array = np.array(master_dict[keymax]["game"])
# # print(game_array)
# # print((new_array*game_array).sum())

