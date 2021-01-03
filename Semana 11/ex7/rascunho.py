def intersection(line1, line2):
    line1_ = [number*line2[1] for number in line1]
    line2_ = [number*line1[1] for number in line2]
    
    if line1[1] == line2[1]:
        return False

    equation = [line1_[0] - line2_[0], line1_[1] - line2_[1],\
                line1_[2] - line2_[2]]

    intersection_y = equation[2] / equation[0]
    intersection_x = (intersection_y - line1[2])/line1[1]
    


    return (intersection_x, intersection_y)


def eq_line(point1, point2):
    delta_y = point1[1] - point2[1]
    delta_x = point1[0] - point2[0]
    
    if delta_x != 0:
        inclination = delta_y/delta_x
        line = [1, inclination, -inclination*point1[0] + point1[1]]
    else:
        line = [0, -1, point1[0]]          
    return line

# print(intersection([1,3,2],[1,2,1]))

print(eq_line([0,2],[8,0]))
