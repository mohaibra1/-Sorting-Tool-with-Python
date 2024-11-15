import sys,argparse, re
from collections import Counter
from io import StringIO

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

arg_parser = CustomArgumentParser(description='Process and sort different types of data.')
arg_parser.add_argument('-sortingType', type=name_type, choices=['natural', 'byCount'],
                        default="natural", help="The type of data to process")
arg_parser.add_argument('-dataType', type=name_type,  choices=['word','line','long'],
                        default="word", help='Type of data to process.')
arg_parser.add_argument('-inputFile', type=str, required=False)
arg_parser.add_argument('-outputFile', type=str, required=False)
args = None
unknowns = None
errr = []
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
    if data_type == 'long' and len(error_holder) > 0:
        print(*error_holder, sep='\n')
    return data

def read_data(data_1, data_type):
    data = []
    for j in data_1:
        if data_type == 'long':
            temp = []
            line = j.split()
            for item in line:
                try:
                    temp.append(int(item))
                except ValueError:
                    errr.append(f"{item} is not a long. It will be skipped.")
            #temp.extend(map(int, line.split()))
            temp = sorted(temp)
            data.extend(temp)
        elif data_type == 'line':
            data.append(j)
        elif data_type == 'word':
            line = j.split()

            data.extend(line)

    # if data_type == 'long' and len(error_holder) > 0:
    #     print(*error_holder, sep='\n')
    return data

def sort_naturally(data, data_type):
    total_count = len(data)
    if data_type == 'long':
        data_type = 'numbers'

    if data_type == 'numbers':
        print(f"Total {data_type}: {total_count}.")
        sorted_data = sorted(data)
        s = " ".join(map(str, sorted_data))
        print(f'Sorted data: {s}')
    elif data_type == 'line':
        print(f"Total {data_type}: {total_count}.")
        data.sort()
        print('Sorted data:')
        print(*data, sep='\n')
    elif data_type == 'word':
        print(f"Total {data_type}: {total_count}.")
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
    global args, unknowns

    if unknowns:
        if len(unknowns) == 1:
            print(f'"{unknowns[0]}" is not a valid parameter. It will be skipped')
        else:
            for j in unknowns:
                print(f'"{j}" is not a valid parameter. It will be skipped')


    if args.inputFile:
        data = []
        with open(args.inputFile, 'r') as f:
            for line in f:
                # remove newlines and spaces
                line = line.strip()
                data.append(line)

        data = read_data(data, args.dataType)

        if args.sortingType == 'byCount':
            sort_by_count(data, args.dataType)
        else:
            if args.dataType == 'long' and len(errr) > 0:
                print(*errr, sep='\n')
            sort_naturally(data, args.dataType)

    else:
        data = check_data_type(args.dataType)
        sort_by_count(data, args.dataType) if args.sortingType == 'byCount' else sort_naturally(data, args.dataType)

def capture_output(func):
    original_output = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    func()

    sys.stdout = sys.__stdout__
    sys.stdout = original_output
    error_list = []
    output_list = []
    for line in captured_output.getvalue().splitlines():
        if unknowns or 'skipped' in line:
            error_list.append(line)
            unknowns.pop()
        else:
            output_list.append(line)

    # for j in error_list:
    #     print(j)

    return output_list, error_list



if __name__ == "__main__":
    try:
        args, unknowns = arg_parser.parse_known_args()
    except SystemExit:
        exit(1)
    lists = None
    if args.outputFile:
        lists = capture_output(main)
        with open(args.outputFile, 'w') as file:
            for i in lists[0]:
                file.write(i + '\n')
        for error in lists[1]:
            print(error)
    else:
        main()
        # original_stdout = sys.stdout
        # c = StringIO()
        # sys.stdout = c
        # main()
        # sys.stdout = sys.__stdout__
        #
        #
        # with open('temp.txt', 'w') as fl:
        #     for holder in c.getvalue().splitlines():
        #         fl.write(f"{holder}\n")
        #
        # with open('lose.txt', 'a') as li:
        #     for holder in c.getvalue().splitlines():
        #         li.write(f"{holder}\n")
        #
        # sys.stdout = original_stdout
        #
        # with open('temp.txt', 'r') as flp:
        #     for system in flp:
        #         system = system.strip()
        #         print(system)
