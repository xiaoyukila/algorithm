def heapSort(num, index):
    print("Heap Sort:")
    print("Origin list:", num[0:index])
    if index == 0:
        return
    print("Construct initial heap:")
    for i in range(index // 2 - 1, -1, -1):
        print(i)
        drill(num, index, i)
        print(num)
    
    print("Sorting...")
    for i in range(index - 1, -1, -1):
        print("get largest number:", num[0])
        swap(num, 0, i)
        print("current list:", num)
        drill(num, i - 1, 0)
    
    print("list sorted:", num)


def drill(num, index, i):
    child = i * 2 + 1
    if child <= index and num[i] < num[child]:
        swap(num, i, child)
        print(num)
        drill(num, index, child)
    child = i * 2 + 2
    if child <= index and num[i] < num[child]:
        swap(num, i, child)
        print(num)
        drill(num, index, child)

def swap(num, i, j):
    print("swap", num[i], " and ", num[j])
    temp = num[i]
    num[i] = num[j]
    num[j] = temp

print("Sort.")
originList = [3,1,6,2,5,8,4,7,9]
heapSort(originList, len(originList))