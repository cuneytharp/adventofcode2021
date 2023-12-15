# -*- coding: utf-8 -*-
with open("day3.txt","r") as file:
    my_list = file.readlines()

my_list = [x.strip() for x in my_list]
copy_list = my_list.copy()
minimum_list = my_list.copy()

for i in range(0,12):
    one= 0
    zero = 0
    for line in my_list: 
        if line[i]=="1":
            one += 1
        else:
            zero +=1 
            
    
    if zero> one:
        decider = "1"
    else:
        decider = "0"
    print("I: ",i ," decider",decider,"uzunluk",len(my_list))
    if i ==10:
        print("GİRİŞ",my_list)
    for line in my_list:
        if line[i]!=decider:
            if len(my_list)==1:
                break
            #list(filter(lambda a: a != line, copy_list))
            my_list = [i for i in my_list if i != line]
            #copy_list.remove(line)
            #print(line)
    if i ==10:
        print("ÇIKIŞ",my_list)
print("MY_LIST",my_list)

# for i in my_dict.keys():
#     if my_dict[i]["0"]<= my_dict[i]["1"]:
#         decider = 0
#     else:
#         decider = 1
#     #print("I: ",i ," decider",decider)
#     for line in my_list:
#         #print("dongu bası:",copy_list)
#         temp_list = [int(x) for x in line]
#         if temp_list[int(i)]==int(decider):
#             pass
#         else:
#             #print("silinecek",line)
#             if line in minimum_list:
#                 minimum_list.remove(line)
#         if len(minimum_list)==1:
#             #print(i," kolonunda döngü bitti")
#             #print("final element",minimum_list)
#             break
#         #print("dongu sonu",minimum_list)
# print(minimum_list)
