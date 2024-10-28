# print 1st n Natural numbers
def nat_num(n):
    if n>0:
        nat_num(n-1)
        print(n)

nat_num(10)

