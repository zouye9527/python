# 折半查找
ist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
print(binary_search(ist, 5))
print(binary_search(ist, 11 ))