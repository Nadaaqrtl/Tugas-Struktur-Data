def squares_sum(n):
    sum = 0
    for i in range(0,n):
        sum = sum + i**2
    return sum

print(squares_sum(12)) 
