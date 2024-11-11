import sys
from collections import Counter


def check_data_type(data_type):
    data = []
    while True:
        try:
            line = input()
            if data_type == 'long' or data_type == '-sortIntegers':
                data.extend(map(int, line.split()))
            elif data_type == 'line':
                data.append(line)
            elif data_type == 'word':
                data.extend(line.split())
        except EOFError:
            break
    return data


def process_data(data, data_type):
    count = len(data)
    if data_type == 'long' or data_type == '-sortIntegers':
        max_item = max(data)
    else:
        max_item = max(data, key=len)

    item_counts = Counter(data)
    max_count = item_counts[max_item]
    percentage = (max_count / count) * 100

    print(f"Total numbers: {count}.")
    if data_type == 'long':
        print(f"The greatest number: {max_item} ({max_count} time(s), {int(percentage)}%).")
    elif data_type == 'line':
        print("The longest line:")
        print(max_item)
        print(f"({max_count} time(s), {int(percentage)}%).")
    elif data_type == 'word':
        print(f"The longest word: {max_item} ({max_count} time(s), {int(percentage)}%).")
    elif data_type == '-sortIntegers':
        data.sort()
        print("Sorted words: ", end='')
        for word in data:
            print(word, end=' ')


def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py -dataType <long|line|word>')
        sys.exit(1)

    # data_type = sys.argv[1]
    #
    # if data_type not in ['long', 'line', 'word']:
    #     print('Invalid data type. Use long, line, or word.')
    #     print(sys.argv[1], '-dataType', '<long|line|word>'  )
    #     sys.exit(1)
    if '-sortIntegers' in sys.argv:
        data = check_data_type('-sortIntegers')
        process_data(data, '-sortIntegers')
    else:
        data_type = sys.argv[2]
        data = check_data_type(data_type)
        process_data(data, data_type)

if __name__ == "__main__":
    main()