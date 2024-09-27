'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)
'''

def insertion_Sort(arr):
    for i in range(1,len((arr))):
        key = arr[i]
        j = i - 1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

if __name__ == '__main__':
    # Array Input
    arr = list(map(int,input().split()))
    rsult = insertion_Sort(arr)
    print(arr)


# big to small code

def InsertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp > list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
if __name__ == '__main__':
    
    list = list(map(int,input().split()))
    InsertionSort(list)
    print("Array after sorting:")
    print(list)
