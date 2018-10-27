def rotate(alist, d, n):
    empty_list = []
    for index in range(d,n):
       value = alist[index]
       empty_list.append(value)
    remaining_list = alist[ :d]
    empty_list.extend(remaining_list)
    return empty_list

test = rotate([2,6,3,8], 3, 4)
print(test)