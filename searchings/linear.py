def linearsearch(list,ele):
    for i in range(len(list)):
        if list[i]==ele:
            return i+1
    return -1
 
list=[23,4,5,67,8,2334]
ele=2334
r=linearsearch(list,ele)
if r==-1:
    print("Element not found")
else:
    print("Element is found at index",r)