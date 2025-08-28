# # 3 Sum

# # def three_sum(arr):
# #     n = len(arr)
# #     num_set = set()

# #     for i in range(n):
# #         for j in range(i+1, n):
# #             for k in range(j+1, n):
# #                 if arr[i] + arr[j] + arr[k] == 0:
# #                     triplet = tuple(sorted([arr[i],arr[j],arr[k]]))
# #                     # ([1 2 4],[1 4 5],[2 5 4])
# #                     num_set.add(triplet)
# #     return [list(triplet) for triplet in num_set]

# # print(three_sum([-1,0,1,2,-1,-4]))

# # Container with Most Water

# def indetify_most_water(arr):
#     n = len(arr)
#     result = 0
#     for i in range(0,n-1):
#         maximum_water = min(arr[i],arr[i+1])
#         width_between__two_lines = (i+1)-i
#         area = maximum_water * width_between__two_lines
#         result = max(result,area)
    
#     return result



# def optimised_most_water(arr):
#     n = len(arr)
#     left = 0
#     right = n-1
#     result = 0

#     while left < right:
#         if arr[left] < arr[right]:
#             max_water_should_contain = arr[left]
#         else:
#             max_water_should_contain = arr[right]
        
#         width = right - left
#         area = max_water_should_contain * width

#         if area > result:
#             result = area

#         if arr[left] < arr[right]:
#             left = left + 1
#         else:
#             right = right - 1
#     return result

# print(optimised_most_water([1,8,6,2,5,4,8,3,7]))



def unique_ones(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] = 1
        else:
            hash_map[arr[i]] = 1
    return len(hash_map)

print(unique_ones([2,2,2,2,2,3,3,3]))