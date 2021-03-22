from typing import final


def all_zero(lst):
    new_list = [str(element) for element in lst]
    num_zero = new_list.count("0")
    


    for i in range(num_zero):
        new_list.remove("0")

    final_list = []

    for i in range(len(new_list)):
        if new_list[i] == "True":
            final_list.append(True)
        elif new_list[i] == "False":
            final_list.append(False)
        else:
            final_list.append(int(new_list[i]))

    final_list = final_list +[0]*num_zero
    return final_list 

lst = [3,1,True,0,2,77,-12,3,False, -5, 0, 1]

print(all_zero(lst))

a = True
print(type(str(a)))