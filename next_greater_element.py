def find_next_gt_elements(array):
    if not array:
        return
    n = len(array)
    output_array = [-1]*n
    stack = [array[-1]]
    for i in range(n-2, -1, -1):
        while stack:
            if stack[-1] > array[i]:
                output_array[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(array[i])
    return output_array

print(find_next_gt_elements([4, 5, 2, 25]))
print(find_next_gt_elements([13, 7, 6, 12]))
print(find_next_gt_elements([1,2,3]))
print(find_next_gt_elements([5,4,3]))
print(find_next_gt_elements([5,4]))