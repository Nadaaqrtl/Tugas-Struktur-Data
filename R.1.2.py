def is_even(k):
    if k == 0 :
        return True
    elif k == 1:
        return False
    else:
        return is_even(k-2)


print(is_even(1000))
