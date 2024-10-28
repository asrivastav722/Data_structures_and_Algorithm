def even_sum(n):
    if n==0:
        return 0
    return 2*n +even_sum(n-1)
       
print(even_sum(5))