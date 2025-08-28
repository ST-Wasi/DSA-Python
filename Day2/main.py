
#  Display the Series 1,2,3,4,5,6…N 
# N = int(input("Enter value of N: "))
# for n in range(1,N+1):
#     print(n)

# Display the Series 1,3,5,7,9…N 
# N = int(input("Enter value of N: "))
# for n in range(1,N+1,2):
#     print(n)

#  Display the Series 4,16,36,64…N 
# N = int(input("Enter value of N: "))
# for n in range(2,N+1,2):
#     print(n*n)


# Display the Series 1,2,4,7,11,16,22…N
# N = int(input("Enter value of N: "))
# num = 1
# diff = 1

# for i in range(N):
#     print(num)
#     num = num + diff
#     diff = diff + 1


# 1 Printing Star Pattern (N Rows)
# *****
# *****
# *****
# *****
# T = int(input("Enter Number of Test Cases: "))
# while T>0:
#     x,y,z = map(int, input().split())
#     total = x*5 + y*10
#     result = total // z
#     print(result)
#     T = T-1
# for n in range(N):
#     print("*****")


# LIst and its Iteration
# 5 Size of the List
# 1 2 3 4 5
# arr = []
# n = int(input("Enter Size of the array: "))
# for i in range(n):
#     x = int(input(f"Enter Element {i+1}: "))
#     arr.append(x)
# print(arr)

# arr = list(map(int, input("Enter List Elements: ").split()))
# # print(arr)

# for i in arr:
#     print(i)

# Two Sum

 # write a function which takes parameter as list ad a target num and it should return another list of integer with idexes of which addition resuting  ==  target
def two_sum(nums , target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i , j]
    return []

print(two_sum([2,7,11,15],9))        