import argparse, re
from collections import Counter

arg_parser = argparse.ArgumentParser(description='Process and sort different types of data.')

def check_data_type(data_type):
    data = []
    while True:
        try:
            line = input()
            if data_type == 'long':
                temp = []
                temp.extend(map(int, line.split()))
                temp = sorted(temp)
                data.extend(temp)
            elif data_type == 'line':
                data.append(line)
            elif data_type == 'word':
                line = line.split()

                data.extend(line)
        except EOFError:
            break
    return data

def sorting(data):
    pass

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

def parse_line(line):
    # Extract numbers from the line as integers
    return [int(num) for num in re.findall(r" ?\d+", line)]

def sort_naturally(data, data_type):
    total_count = len(data)
    print(f"Total {data_type}: {total_count}.")
    if data_type == 'long':
        sorted_data = sorted(data)
        print(f'Sorted data: {" ".join(map(str, sorted_data))}')
    elif data_type == 'line':
        # sorted_data = sorted(data, key=parse_line)
        # print(f'Sorted data: ')
        # for i in sorted_data:
        #     print(i)
        data.sort()
        print('Sorted data:')
        print(*data, sep='\n')
    elif data_type == 'word':
        converted_data = [int(num) for num in data]
        sorted_data = sorted(converted_data)
        print(f'Sorted data: {" ".join(map(str, sorted_data))}')

def sort_by_count(data, data_type):
    temp = [] # Temporary list to store data
    if data_type == 'long':
        temp = data.copy()  # Copy data to temporary list
    elif data_type == 'line':
        #temp = sorted(data, key=parse_line)
        count = len(data)
        print(f"Total {data_type}: {count}")
        groups = dict()
        for item in data:
            groups[item] = groups.get(item, 0) + 1

        group_list = [(key, val) for (key, val) in groups.items()]
        group_list = sorted(group_list, key=lambda group: group[0])
        group_list = sorted(group_list, key=lambda group: group[1])
        for group in group_list:
            print(f'{group[0]}: {group[1]} time(s), {(group[1] * 100) // count}%')
        return
    elif data_type == 'word':
        for item in data:
            if item != ' ':
                temp.append(item)


    dict_temp = {}
    for item in temp:
        if item in dict_temp:
            dict_temp.pop(item)
        count = temp.count(item)
        dict_temp[item] = count

    total_count = len(temp)
    if data_type == 'long':
        data_type = 'numbers'
    elif data_type == 'line':
        data_type = 'lines'
    else:
        data_type = 'words'
    print(f"Total {data_type}: {total_count}")
    if data_type == 'numbers':
        sorted_dict = dict(sorted(dict_temp.items(), key=lambda x: (x[1], x[0])))
        for item, count in sorted_dict.items():
            percentage = int((count / total_count) * 100)
            print(f"{item}: {count} time(s), {percentage}%")
    elif data_type == 'words':
        sorted_dict = dict(sorted(dict_temp.items(), key=lambda x: (x[1], x[0])))
        for item, count in sorted_dict.items():
            percentage = int((count / total_count) * 100)
            print(f"{item}: {count} time(s), {percentage}%")
    # elif data_type == 'lines':
    #     for item, count in dict_temp.items():
    #         percentage = int((count / total_count) * 100)
    #         print(f"{item}: {count} time(s), {percentage}%")

def main():
    arg_parser.add_argument('-sortingType', type=str, default='natural',
                            help="The type of data to process")
    arg_parser.add_argument('-dataType',type=str, default='word', help='Type of data to process.')
    args = arg_parser.parse_args()

    data = check_data_type(args.dataType)
    sort_by_count(data, args.dataType) if args.sortingType == 'byCount' else sort_naturally(data, args.dataType)

if __name__ == "__main__":
    main()