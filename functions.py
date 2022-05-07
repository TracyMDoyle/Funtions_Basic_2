# 1 Countdown - Create a function that accepts a number 
# as an input. Return a new list that counts down by 
# one, from the number (as the 0th element) down to 0 
# (as the last element).

print("number 1 countdown")
def count_down(num):
    numbers = []
    for x in range (num, -1, -1):
        numbers.append(x)        
    return(numbers)

print(count_down(10))

# 2. Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# def number(num):
print("number 2 print an return")

def number_acceptor(num1, num2):
    print(num1)
    return(num2)

number_acceptor(5,7)
    

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
print("number 3 first plus length")
def list_math(list):
    return list[0] + len(list)

print(list_math([1,2,3,4,5]))


# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

print("number 4 greater than second")
def greater_than_second(list):
    if len(list) < 2:
        return False 
    newList = []
    for x in range(0,len(list)):
        if list[1] < list[x]:
            newList.append(list[x])
    return newList
        

print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
print("number 5 size and value")
def size_value(size, value):
    list = []
    for x in range(0, size):
        len(list) == size
        list.append(value)
    return list
        
print(size_value(4,7))
print(size_value(5,10))