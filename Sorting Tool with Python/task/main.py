import sys,argparse, re
from collections import Counter



class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        if '-sortingType' in message:
            message = 'No sorting type defined!'
        elif '-dataType' in message:
            message = 'No data type defined!'
        print(f"{message}")
        self.exit(2)

def name_type(value):
    if not value or value.strip() == '':
        raise argparse.ArgumentTypeError(f"{value}")
    return value

def check_data_type(data_type):
    data = []
    error_holder = []
    while True:
        try:
            line = input()
            if data_type == 'long':
                temp = []
                line = line.split()
                for item in line:
                    try:
                        temp.append(int(item))
                    except ValueError:
                        error_holder.append(f"{item} is not a long. It will be skipped.")
                #temp.extend(map(int, line.split()))
                temp = sorted(temp)
                data.extend(temp)
            elif data_type == 'line':
                data.append(line)
            elif data_type == 'word':
                line = line.split()

                data.extend(line)
        except EOFError:
            break
    if data_type == 'long':
        print(*error_holder, sep='\n')
    return data

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
    args = None
    unknowns = None
    arg_parser = CustomArgumentParser(description='Process and sort different types of data.')
    arg_parser.add_argument('-sortingType', type=name_type, choices=['natural', 'byCount'],
                            default="natural", help="The type of data to process")
    arg_parser.add_argument('-dataType', type=name_type,  choices=['word','line','long'],
                            default="word", help='Type of data to process.')
    try:
        args, unknowns = arg_parser.parse_known_args()
    except SystemExit:
        exit(1)

    if unknowns:
        if len(unknowns) == 1:
            print(f'"{unknowns[0]}" is not a valid parameter. It will be skipped', end='')
        else:
            for i in unknowns:
                print(f'"{i}" is not a valid parameter. It will be skipped')

    data = check_data_type(args.dataType)
    sort_by_count(data, args.dataType) if args.sortingType == 'byCount' else sort_naturally(data, args.dataType)

if __name__ == "__main__":
    main()