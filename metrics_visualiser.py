import ast
import re

red = '\033[91m'
green = '\033[93m'
value_color = '\033[92m'
default = '\033[0m'

def read_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    start_index = data.index('# small database\n') + 1
    data = ''.join(data[start_index:])
    return data

def parse_data(data, database, col):
    parsed_data = {}
    for match in re.finditer(r'(' + database + '_\w+)\s+=\s+(\[\[.*?\]\])', data):
        test_name = match.group(1)
        test_data = ast.literal_eval(match.group(2))
        parsed_data[test_name] = {'1 Worker': test_data[0][col], '2 Workers': test_data[1][col], '4 Workers': test_data[2][col]}
    return parsed_data

def print_table(influx_data, timescale_data, metric, new_green, new_red):
    print('\n' + ' ' * 36 + metric + ' per worker' + '\n')
    print(' ' * 35 + 'Database' + ' ' * 5 + '1 Worker' + ' ' * 10 + '2 Workers' + ' ' * 9 + '4 Workers')
    print('+--------------------------------+------------+-----------------+-----------------+-----------------+')
    for test_name in influx_data.keys():
        print('|', test_name.ljust(30), '|', green + 'Influx'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers']:
            influx_val = influx_data[test_name][worker]
            timescale_val = timescale_data[test_name][worker]
            percentage = round(influx_val / timescale_val * 100)
            color_code = new_red if percentage > 100 else new_green  # red if percentage > 100 else green
            print('|',(f"{value_color}{influx_val} {color_code}({percentage}%)").ljust(25) + default, end=' ')
        print('|')
        print('|', ''.ljust(30), '|', red + 'Timescale'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers']:
            timescale_val = timescale_data[test_name][worker]
            print('|', value_color + str(timescale_val).ljust(15) + default, end=' ')
        print('|')
        print('+--------------------------------+------------+-----------------+-----------------+-----------------+')

timescale_data = read_data('timescale.py')
influx_data = read_data('influx.py')

metric = ['Wall Clock Time (s)', 'Queries per second', 'User Time (s)', 'System Time (s)', 'CPU Usage (%)']
databases = ['small', 'medium', 'big']

for database in databases:
    for col in range(5):
        if col == 1:
            new_green = '\033[91m'
            new_red = '\033[93m'
        else:
            new_green = '\033[93m'
            new_red = '\033[91m'
        parsed_timescale_data = parse_data(timescale_data, database, col)
        parsed_influx_data = parse_data(influx_data, database, col)
        print_table(parsed_influx_data, parsed_timescale_data, metric[col], new_green, new_red)
