# How we can take inputs in python
# Jay and Jafina Problem


# x = int(input("Enter the value of Number of 5 Ruppees Coins:  "))
# y = int(input("Enter the value of Number of 10 Rupees coins : "))
# z = int(input("Enter the price of each choclate: "))
# x,y,z = map(int, input().split())
# total = x*5 + y*10

# # amount_with_five_rupees = x*5
# # amount_with_ten_rupees = y*10
# # total_amount = amount_with_five_rupees + amount_with_ten_rupees
# result = total // z
# print(result)

# def addition(x,y):
#     print(x+y)


# addition(2,2)

# add = lambda x,y:print(x+y)
# hello = lambda: print("Hello World")

# add(50,50)
# hello()


def find_number_of_ways(number_of_candies):
    number_of_ways = 0
    
    for start in range(1,number_of_candies+1,2):
        total = 0
        current = start
        while total < number_of_candies:
            total = total + current 
            current += 2
            if total == number_of_candies:
                number_of_ways += 1
                break

    return number_of_ways
    
number_of_candies_girl_wants = int(input("Enter the value of what amount of candied girl want: "))

print(find_number_of_ways(number_of_candies_girl_wants))
            # total += current
    # consecutive and it should be distinct
