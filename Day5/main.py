
# list_of_numbers_made_of_even_value = []
# def has_even_numbers(num):
#     num_str = str(num)
#     for digit in num_str:
#         if int(digit) % 2 != 0:
#             return False
    
#     return True


# for i in range(1,11):
#     if(has_even_numbers(i)):
#         list_of_numbers_made_of_even_value.append(i)


#Recursion BAsics

# print Number 1 to N (Loops SOlution)

# N = int(input())
# for i in range(1,N+1):
#     print(i)

# print Number 1 to N (Recursion)

# def print_nummbers(N):
#     if N == 0:
#         return
#     print_nummbers(N-1)
#     print(N)

# print_nummbers(5)

# Factorial till N (Loops Solution)

# N = int(input())
# fact = 1
# for i in range(1,N+1):
#     fact = fact * i

# print(fact)

# Factorial till N (Recursive Solution)

# def factorial(N):
#     if N == 1:
#         return 1
#     return N * factorial(N-1)

# print(factorial(5))

# Fibonacci Series (Loops Version)

# n = 5
# a , b = 0 , 1
# for i in range(n):
#     print(a)
#     sum = a + b
#     a = b
#     b = sum


# Fibonacci Series (Recursion Version)

# def fibonacci(n):
#     if n == 0: # base case
#         return 0
#     if n == 1: # base case
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# for i in range(5):
#     print(fibonacci(i))

# def isSafe(board, row, col, n):
#     # Horizontally safe check
#     for j in range(n):
#         if board[row][j] == "Q":
#             return False
    
#     # Vertically Safe Check
#     for i in range(n):
#         if board[i][col] == "Q":
#             return False
    
#     # Right Diagonal safe check
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j] == "Q":
#             return False
#         i = i - 1
#         j = j + 1

#     # Left Diagonal safe check
#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j] == "Q":
#             return False
#         i = i - 1
#         j = j - 1

#     return True


# def solveNQueens(board, row, n, solution):
#     if row == n:
#         solution.append(["".join(r) for r in board])
#         return
    
#     for col in range(n):
#         if isSafe(board, row, col, n):
#             board[row][col] = "Q"
#             solveNQueens(board, row + 1, n, solution)
#             board[row][col] = "."  # back track


# def main_function(n):
#     board = [["." for _ in range(n)] for _ in range(n)]
#     solution = []
#     solveNQueens(board, 0, n, solution)
#     return solution


# n = 4
# solution = main_function(n)

# for idx, sol in enumerate(solution, 1):
#     # print(f"{idx}: ")
#     for row in sol:
#         print(row)
#     print()

def firstUniqChar(s):
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] = char_count[char] + 1
            else:
                char_count[char] = 1
        for i in range(len(s)):
            char = s[i] 
            if char_count[char] == 1:
                return i  
        return -1