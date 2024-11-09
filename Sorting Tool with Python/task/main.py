import sys

numbers = [] # List to store the numbers
lines = [] # List to store the lines
words = [] # List to store the words

if len(sys.argv) < 3:
    print('Usage: python script.py <data_type> <long|line|word>')
    sys.exit(1)

data_type = sys.argv[2] # Get the data type from the command line argument

def check_data_type():
    while True:
        temp = [] # Temporary list to store the numbers before checking the data type
        try:
            data = input() # Get user input
            if data_type == 'long':
                data = data.split() # Split the input into words
                temp = [int(x) for x in data] # Convert strings to integers and create a list
                numbers.extend(temp) # Add the numbers to the list
            elif data_type == 'line':
                lines.append(data) # Add the line to the list
            elif data_type == 'word':
                data = data.split() # Split the input into words
                temp = [x for x in data] # Create a list of words
                words.extend(temp) # Add the words to the list
        except EOFError:
            break
    if data_type == 'long':
        for_long()
    elif data_type == 'line':
        for_line()
    elif data_type == 'word':
        for_word()

def for_long():
    length = len(numbers) # Calculate the total number of numbers
    print(f'Total numbers: {len(numbers)}.')
    times = numbers.count(max(numbers)) # Count the number of occurrences of the maximum number
    percentage = (times / length) * 100 # Calculate the percentage of numbers with the maximum value
    print(f"The greatest number: {max(numbers)} ({times} time(s), {int(percentage)}%).")

def for_line():
    length = len(lines) # Calculate the total length of all lines
    print(f'Total lines: {length}')
    times = max(lines, key=len) # Find the line with the maximum length
    times = lines.count(times) # Count the number of occurrences of the longest line
    percentage = (times / length) * 100 # Calculate the percentage of lines with the maximum length
    print("The longest line: ")
    print(f"{max(lines, key=len)}")
    print(f"({times} time(s), {int(percentage)}%).")

def for_word():
    length = len(words) # Calculate the total number of words
    print(f'Total words: {len(words)}.')
    times = max(words, key=len) # Find the word with the maximum length
    times = words.count(times)
    percentage = (times / length) * 100 # Calculate the percentage of words with the maximum length
    print(f"The longest word: {max(words, key=len)} ({times} time(s), {int(percentage)}%).")

check_data_type()