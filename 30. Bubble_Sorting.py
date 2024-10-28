# Bubble Sort Program
def bubble_sort(array):
    x=0
    y=0
    while y < len(array): 
        while x < len(array)-1-y:
            if array[x]>array[x+1]:
                temp=array[x+1]
                array[x+1]=array[x]
                array[x]=temp
            x=x+1
            print(array)
        x=0
        y=y+1
    return array

# Modified Bubble Sort Program 
def mbubble_sort(array):
    x=0
    y=0
    print(array)
    while y < len(array):
        if is_sorted(array):
            break
        else: 
            while x < len(array)-1-y:
                if array[x]>array[x+1]:
                    temp=array[x+1]
                    array[x+1]=array[x]
                    array[x]=temp
                x=x+1
            x=0
        print(array)
        y=y+1
    return array
#To check the array is sorted or not
def is_sorted(array):
    x=0
    y=1
    flag=1
    while x < len(array)-1:
        y=x
        while y <len(array)-1:
            if array[x]>array[y]:
                flag=0
                break
            y=y+1
        y=0
        x=x+1
    if flag==0:
        return False
    else:
        return True

list=[89,88,46,29,11,60,10,25,69,50]
print(is_sorted(list))
print(mbubble_sort(list))
print(is_sorted(list))






