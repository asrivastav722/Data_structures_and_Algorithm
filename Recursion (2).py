# print 1st n Natural numbers in reverse order
def natr_num(n):
    if n!=0:
        print(n)
        natr_num(n-1)

natr_num(10)
