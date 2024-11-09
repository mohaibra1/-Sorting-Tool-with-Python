numbers = [] # List to store the numbers
while True:
    try:
        data = input().split() # Get user input
        temp = [int(x) for x in data] # Convert strings to integers and create a list
        numbers.extend(temp) # Add the numbers to the list
    except EOFError:
        break

print(f'Total numbers: {len(numbers)}')
times = numbers.count(max(numbers)) # Count the number of occurrences of the maximum number
print(f"The greatest number: {max(numbers)} ({times} time(s))")