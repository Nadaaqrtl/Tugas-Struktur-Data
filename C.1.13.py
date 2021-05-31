def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.prepend(list[len(list)-i-1])
    return reversed_array

print(reverse_list_of_integers([2,4,5,6,7,8]))
