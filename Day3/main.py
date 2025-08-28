# nums = [1,2,3,4,5,6,7,8,9,10]
# target = 15
# result = -1
# for num in nums:
#     if(num == target):
#         result = num
#         break 
# print(result)

# A Watermelon - Codeforces

# N = int(input())
# if (N%2 == 0):
#     print("YES")
# else:
#     print("NO")





# Binary Search

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if(target == arr[mid]):
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# bubble Sort

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubble_sort([44,0,2,2,0,2,5,10,100]))

# Waved Array

# def get_waved_array(arr):
#     arr.sort()
#     for i in range(0,len(arr)-1,2):
#         arr[i] = arr[i+1]
#         arr[i+1] = arr[i]
#     return arr

# Given a string: String == "YeS" ? "YES" : "NO"

# def check_yes_or_no(string):
#     if string.upper() == "YES":
#         print("YES")
#     else:
#         print("NO")

# def two_sum_with_dict(arr, target):
#     new_map = {}
#     for i, element in enumerate(arr):
#         diff = target - element
#         if diff in new_map:
#             return [new_map[diff],i]
#         new_map[element] = i
#     return []


# Binary Search with Recursion:

# def binary_search_with_recursion(arr,target):
#     start = 0
#     end = len(arr)- 1
#     mid = len(arr) //2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search_with_recursion(arr[:mid],target)
#     else:
#         res = binary_search_with_recursion(arr[mid+1:],target)
#         return mid + 1 + res if res != -1 else -1



# Selection Sort

# def selection_sort(arr):
    
#     for n in range(len(arr)):
#         min_index = n
#         for j in range(n+1,len(arr)):
#             if arr[j] <arr[min_index]:
#                 min_index = j
#         arr[n], arr[min_index] = arr[min_index],arr[n]

#     return arr

# print(selection_sort([24,51,0,5,21,10,8]))


def merge_sort(numbers):
    n = len(numbers)
    if(n <= 1):
        return numbers

    # finding the mid element
    mid = n // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted,right_sorted)

    # return 

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
