def isPalindrome(x):
    list1=[]
    len_list = len(str(x))
    for i in range(0,len_list):
        list1.append(x%10)
        x=x/10
    for i in range(0,int(len_list/2)):
        if list1[i] != list1[len_list-i-1]:
            return False
    return True

print(isPalindrome(121))
