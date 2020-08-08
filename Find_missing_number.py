def find_missing_number_in_n(array):
    xor_whole = 1
    for i in range(2, len(array)+2):
        xor_whole ^= i

    xor_array = array[0]
    for i in range(1, len(array)):
        xor_array ^= array[i]

    return xor_array ^ xor_whole

array = [1,2,4,5,6]
print(find_missing_number_in_n(array))
