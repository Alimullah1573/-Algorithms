
'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)
'''


'''def selection_sort(arr,size):
    for i in range(size):
        main_index = i
        for j in range(i+1,size):
            if arr[j] < arr[main_index]:
                main_index = j
        arr[i],arr [main_index] = arr[main_index],arr[i]

arr = list(map(int,input().split()))
size  = len(arr)
selection_sort(arr,size)

'''


# Class Function
"""
class Solution:
    def select(self, arr, i):
        pass
    def selectionSort(self, arr, n):
        for i in range(0, n):
            main_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[main_index]:
                    main_index = j
            if main_index != i:
                arr[i], arr[main_index] = arr[main_index], arr[i]
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        Solution().selectionSort(arr,n)
        print(*arr)"""





# BIg To small Algorithms
'''def selecton_sort(arr,n):
    for i in range(n):
        main_index = i
        for j in range(i+1,n):
            if arr[j]>arr[main_index]:
                main_index = j

        arr[i],arr[main_index] = arr[main_index],arr[i]

if __name__ == '__main__':
    arr = [2,3,4,1]
    n = len(arr)
    selecton_sort(arr,n)
    print(arr)


'''




