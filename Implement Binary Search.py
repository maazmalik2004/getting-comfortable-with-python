def binarySearch(list, target):
    left, right = 0,len(list)-1
    while left <= right:
        mid = (right+left)//2
        if list[mid]==target:
            return mid
        elif list[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return None

myList = [1,2,3,4,5,6,7]
print(binarySearch(myList, 5))
print(binarySearch(myList, 13))