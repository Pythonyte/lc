class TestInvoke(object):
    def __init__(self):
        print("in init")
        self.val = 10
    def __call__(self, *args, **kwargs):
        print("in call")
        return 10


t = TestInvoke()
t()

a = [1,4,6]
b = [1,2,3,5,6,7,8,9]

def find_values_v1(source_arr, target_arr):
    source_arr_mapping = {val:True for val in source_arr}
    return [val for val in target_arr if val not in source_arr_mapping]

def find_values_v2(source_arr, target_arr):
    source_set = set(source_arr)
    source_set.intersection(set(target_arr))
    return source_set

# in a not in b
print(find_values_v2(a,b))

# in b not in a
print(find_values_v2(b,a))

from array import array
a = array("i", [1])
a.append(2)
print(a)