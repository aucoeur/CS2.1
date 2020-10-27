# def is_sorted(items):
#     #TODO: return a bool indicating whether the items are sorted or not
#     for index in range(len(items)-1):
#         if items[index] >= items[index+1]:
#             return False
#     return True

def is_sorted(items):
    # O(n) linear  because looks at everything once 
    for index, item in enumerate(items[:-1]):
        if item > items[index+1]:
            return False
    return True

print(is_sorted([1,3,5,10,20]))#expecting True
print(is_sorted([20,3,5,10,1]))#expecting False