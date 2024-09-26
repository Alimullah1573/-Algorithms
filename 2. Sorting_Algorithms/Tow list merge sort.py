
'''
    Time Complexity     : O(nlog n)
    Space Complexity    : O(n)

    Best Cases          : O(nlog n)
    Average Cases       : O(nlog n)
    Worst Cases         : O(nlog n)

'''

"""def merge_sort(list_A,list_B):
    len_a = len(list_A)
    leb_b = len(list_B)
    i = j = 0
    new_list = []

    while i<len_a and j<leb_b:
        if list_A[i] <= list_B[j] :
            new_list.append(list_A[i])
            i+=1
        else:
            new_list.append(list_B[j])
            j+=1

    while i<len_a:
        new_list.append(list_A[i])
        i += 1
    while j<leb_b:
        new_list.append(list_B[j])
        j+=1
    return new_list
if __name__ == '__main__':

    # Input Array
    list_A = list(map(int,input().split()))
    list_B = list(map(int,input().split()))
    print(merge_sort(list_A,list_B))"""

    # Other's Systems
    # list_A.sort()
    # list_B.sort()
    #print(merge_sort(list_A, list_B))



#**************************************
# Class Function
class Solution:
    def merge(self, arr1, arr2, n, m):
        i = n - 1
        j = 0

        while j < m and i > -1 and arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i = i - 1
            j = j + 1
        arr1.sort()
        arr2.sort()
if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int,input().split())
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        ob = Solution()
        ob.merge(arr1,arr2,n,m)
        print(*arr1)
        print(*arr2)