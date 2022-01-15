cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"This is the original order of the list 'cars': {cars}")

print(f"\nThis is the sorted list 'cars': {sorted(cars)}")

print(f"\nThis is the reversed sorted list 'cars': {sorted(cars,reverse=True)}")

print(f"\nThis is the original list 'cars' again: {cars}")

cars.sort()
print(f"\nNow, the list is going to be permanently sorted: {cars}")

print(f"Printing the list: {cars}")

cars.sort(reverse=True)
print(f"\nAnd then, list reversed sorted:\n\t{cars}")

print(f"Printing the list: {cars}")

cars.reverse()
print(f"\nReverse once: {cars}")

cars.reverse()
print(f"\nReverse twice (undo 'reverse'): {cars}")

print(f"\nThe length of the list is: {len(cars)}")