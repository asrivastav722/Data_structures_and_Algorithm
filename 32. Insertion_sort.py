def insertion_sort(list):
    x=0
    while x<len(list)-1:
        i=x
        while i>=0:
            temp=list[i+1]
            if list[i]>temp:
                list[i+1]=list[i]
                list[i]=temp
            else:break
            i=i-1
        x=x+1
    return list


list=[50,20,37,91,64,18,43,59,72,81]
print(list)
print(insertion_sort(list))
