def shellsort(array,size):
    g=size//2
    while(g>0):
        for i in range(g,size):
            y=array[i]
            z=i
            while z>=g and array[z-g] >y:
                array[z]=array[z-g]
                z-=g
            array[z] = y
        g=g//2

array=[23,12,1,17,45,2,13]
size=len(array)
shellsort(array,size)
print(array)