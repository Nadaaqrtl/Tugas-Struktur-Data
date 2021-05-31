def squared_odd_sum(n):
    sum = 0
    for number in range(n):
        if number%2 == 0:
            continue
        sum =sum + number**2
    return sum

print(squared_odd_sum(12))
