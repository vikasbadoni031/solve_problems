def mergeTwoLists(list1,list2):
    c_1=0
    c_2=0
    list3 = []
    while c_1 < len(list1) and c_2 < len(list2):
        if list1[c_1] >= list2[c_2]:
            list3.append(list2[c_2])
            c_2 = c_2 + 1
        elif list1[c_1] < list2[c_2]:
            list3.append(list1[c_1])
            c_1 = c_1 + 1
    
    if c_1 > len(list1)-1:
        list3 = list3 + list2[c_2:]
    else:
        list3 = list3 + list1[c_1:]
    return list3



list1 = [4,9,20]
list2 = [1,2,9,10]



print(mergeTwoLists(list1,list2))


