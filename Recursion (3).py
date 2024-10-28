# print 1st n odd natural numbers
def odd_num(n):
    if 0<=n:
        
        odd_num(n-1)
        if n%2==0:print(n)

odd_num(10)