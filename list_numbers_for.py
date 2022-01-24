# listing numbers with range()
for value in range(1, 6):
    print(value)
# introducing some space
print("\n")
# listing numbers with range() without starting number
for value in range(4):
    print(value)
# introducing some space
print("\n")
# creating a list of numbers with range()
numbers_list = list(range(1,6))
print(numbers_list)
# introducing some space
print("\n")
# creating a list of even numbers with range()
even_numbers_list = list(range(2,11,2))
print(even_numbers_list)
# introducing some space
print("\n")
# creating a list of squares between 1 and 10
squares_numbers_list = []
for value in range(1,11):
    squares_numbers_list.append(value**2)
print(squares_numbers_list)
# introducing some space
print("\n")
# checking statistics from squares list
print(f"The minimum number from the squares list is: {min(squares_numbers_list)}")
print(f"The maximum number from the squares list is: {max(squares_numbers_list)}")
print(f"The sum from the numbers of squares list is: {sum(squares_numbers_list)}")
# introducing some space
print("\n")
# working with list comprehensions
squares = [value ** 2 for value in range(1,11)]
print(squares)
million_numbers = list(range(0,1_000_001))
sum = sum(million_numbers)
print(sum)
odd_numbers_cubes = [value ** 3 for value in range(1,10,2)]
print(odd_numbers_cubes)