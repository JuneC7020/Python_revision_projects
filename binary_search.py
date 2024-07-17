import sys, random

def search(list, target):
    left = 0
    right = len(list) - 1
    avg = int((left + right)/2)
    while (left < right):
        if (list[avg] == target):
            return avg
        elif (list[avg] < target):
            return avg + 1 + search(list[avg+1:], target)
        else:
            return search(list[:avg], target)
    
    print("The target value is at ", avg, " of the sorted list.")


def createRandomSortedList(num, start = 1, end = 1000):
    arr = []
    tmp = random.randint(start,end)

    for x in range(num):
        while tmp in arr:
            tmp = random.randint(start, end)
        arr.append(tmp)

    arr.sort()
    return arr

def main():
    length = int(input("Enter the lenght of the sorted list(less than 500): "))
    sorted_list =  createRandomSortedList(length)
    print("Sorted list generated: ",sorted_list)
    target = int(input("Enter the target number that you want to search in the sorted list: "))
    print(search(sorted_list, target))

if __name__ =='__main__':
    main()
    