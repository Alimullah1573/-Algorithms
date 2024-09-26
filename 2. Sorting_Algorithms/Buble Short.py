'''
    Time Complexity     : O(n^2)
    Space Complexity    : O(1)


    Best Case           : O(n)

    Worst Case          : O(n^2)
    Average Case        : O(n^2)
'''

"""def Bubleshort(array):
    n  = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
if __name__ == '__main__':
    array = list(map(int,input().split()))
    Bubleshort(array)
    print('Sorted array is :')
    for i in range(len(array)):
        print('%d'%array[i])
"""

# big to small code
'''def Bubleshort(array):
    n  = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] < array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
if __name__ == '__main__':
    array  = list(map(int,input().split()))
    Bubleshort(array)
    print(array)


'''


