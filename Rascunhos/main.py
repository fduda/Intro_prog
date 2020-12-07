def find_x(lst, x):

    mid = int(len(lst)/2) #The mid index
    start = 0 #The starting index
    end = len(lst)-1 #The end index

    # as long as I'm in the sublist- look for the x
    while mid >= start and mid <= end:
        # if the number I'm looking for is smaller than lst[mid]
        #   look for it below the mid
        if lst[mid] > x:
            end = mid - 1
            mid = int((start + end)/2)

        # if larger than update the start to mid+1
        elif lst[mid] < x:
            start = mid + 1
            mid = int((start + end) / 2)
        else:
            return True,mid
    return False

print(find_x(list(range(101)), 12))
print(find_x([1,2,5,7,12], 3))
