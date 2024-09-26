
'''
    Time Complexity     : O(n)
    Space Complexity    : O(1)

    Best Cases          : O(1)
    Average Cases       : O(n)
    Worst Cases         : O(n)

'''
def Linear_Search(li, t):
    n = len(li)
    for i in range(n):
        if li[i] == t:
            return i

    else:
        return 'sorry t is not found!'


# Driver Code
if __name__ == '__main__':
    li = [1, 4, 2, 5, 3]
    t = int(input())
    res = Linear_Search(li, t)
    print(res)

def leaneear_surch(Libaray,t):
   n = len(libaray)
    #print(n)
   for book in range(n):
       #print(book)


        if libaray[book] == t:
            print(t)
            break
   else:
        print('Sorry t is not found')


if __name__ == '__main__':
    libaray = ['a','b','c','d','e','f']
    t = 'v'
    leaneear_surch(libaray,t)


