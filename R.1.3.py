def minmax(data):
    smallest = largest = data[0]
    for data_i in data:
        if smallest > data_i:
            smallest = data_i
        if largest < data_i:
            largest = data_i
    return (smallest, largest)


print(minmax([12,2,2000]))
