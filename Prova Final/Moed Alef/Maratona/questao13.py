from typing import final


string = "  abc d11 3    126 "

def split(string):
    # string = string.strip()

    inter_list = []

    mid_list = []
    for char in string:
        if char != " ":
            mid_list.append(char)
        else:
            inter_list.append(mid_list)
            mid_list = []
    
    inter_list = [i for i in inter_list if len(i) > 0]

    final_list = []
    for i in inter_list:
        joint_string = ""
        for j in i:
            joint_string += j
        final_list.append(joint_string)

    return final_list

print(split(string))

