def odd_sum(n):
    if n==1:
        return 1
    return 2*n-1 +odd_sum(n-1)
       
print(odd_sum(10))