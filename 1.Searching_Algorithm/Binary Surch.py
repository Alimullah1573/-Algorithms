# '''
#     Time Complexity     : O(log n)
#     Space Complexity    : O(1)
#
#     Best Cases          : ---
#     Average Cases       : ---
#     Worst Cases         : ---
#
# '''



"""arr = [1,2,3,4,5,6]
laf = 0
right = len(arr)-1
items = int(input())
while laf<=r
    middil = (laf+righight:t)//2

    if arr[middil] == items:
        print(middil)
        exit()#
    elif arr[middil]<items:
        laf = middil+1
    elif arr[middil]>items:
        right = middil-1
print('Not found items')
"""

'''
arr = [1,2,3,4,5,6]
laf = 0
right = len(arr)-1
items = int(input())
while laf<=right:
    middil = (laf+right)//2

    if arr[middil] == items:
        print(middil)
        exit()
    elif arr[laf] == items:
        print(laf)
        exit()
    elif arr[right] == items:
        print(right)
        exit()
    elif arr[middil]<items:
        laf = middil +1#
    elif arr[middil]>items:
        right = middil-1
print('NOT Found')
'''


# Competitive Problems 1 Solution
'''class Solution:
    def binarysearch(self, arr, n, k):
        lapt, right = 0, len(arr)-1

        while lapt <= right:
            midile = (lapt + right) // 2
            if arr[midile] == k:
                return midile
            elif arr[midile] < k:
                lapt = midile + 1
            else:
                right = midile - 1
        return -1

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        print(ob.binarysearch(arr,n,k))'''

'''
    Time Complexity     : O(log n)
    Space Complexity    : O(1)

    Best Cases          : ---
    Average Cases       : ---
    Worst Cases         : ---

'''


# Iterative implementation of Binary Search
def Binary_Search(li, t):
    left = 0
    right = len(li) - 1

    while left <= right:

        mid = left + (right - left) // 2
        if li[mid] == t:
            return mid

        elif li[mid] < t:
            left = mid + 1

        else:
            right = mid - 1

    else:
        return 'sorry t is not found!'


# Driver Code
if __name__ == '__main__':
    # Sorted Array
    li = [1, 3, 5, 7, 9]
    t = int(input())
    res = Binary_Search(li, t)
    print(res)

'''
# Python3 Program for recursive binary search.

def binarySearch (arr, left, right, x):

	if right >= left:

		mid = left + (right - left) // 2


		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binarySearch(arr, left, mid-1, x)

		else:
			return binarySearch(arr, mid + 1, right, x)

	else:

		return -1

# Driver Code
if __name__ == '__main__':

	arr = [ 2, 3, 4, 10, 40 ]
	x = 10

	left = 0
	right = len(arr) - 1

	# Function call
	result = binarySearch(arr, left, right, x)

	if result != -1:
		print ("Element is present at index % d" % result)
	else:
		print ("Element is not present in array")
'''