def sel_sort(list):
    x=0
    while x<len(list)-1:
        sm_index=smallest(list,x)
        temp=list[x]
        list[x]=list[sm_index]
        list[sm_index]=temp
        print(list)
        x=x+1

def smallest(list,item_index=None):
    start_index=item_index+1
    cache=start_index
    count=0
    got=0
    while item_index <=len(list)-1:
        while start_index<=len(list)-1:
            if list[item_index]<=list[start_index]:
                count=count+1
                if count == len(list)-cache:
                    got=False
                    return item_index
                    break
            start_index=start_index+1   
        start_index=cache
        if got is False: break
        count=0
        item_index=item_index+1

                
list=[89,88,46,29,11,60,10,25,69,50]
sel_sort(list)
# find_smallest(list)