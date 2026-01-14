# 顺序查找
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def seq_search(list, item):
    pos = 0
    found = False
    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found
print(seq_search(list, 5))
print(seq_search(list, 15))