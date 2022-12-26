def selsort(array,size):
    for i in range(size):
        minimum = i
        for j in range(i+1,size):
            if array[j] < array[minimum]:
                minimum = j
        array[i],array[minimum] = array[minimum],array[i]

array = [34,23,1,67,4]
size = len(array)
selsort(array,size)
print(array)