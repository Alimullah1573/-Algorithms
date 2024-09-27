'''
    Best Sorting algorithms is Merge sort.

    Time Complexity     : O(n log n)
    Space Complexity    : O(n)
'''

def mergesort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k] = left_list[i]
                i +=1
            else:
                list1[k] = right_list[j]
                j +=1
            k +=1
        while i<len(left_list):
            list1[k] = left_list[i]
            i +=1
            k +=1
        while j<len(left_list):
            list1[k] = right_list[j]
            j +=1
            k +=1
if __name__ == '__main__':

    num = int(input('How many element you want in list:  '))
    list1 = [int(input()) for x in range (num)]
    mergesort(list1)
    print('Sorted list is : ',list1)

