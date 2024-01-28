"""
This script visualizes metrics for two time-series databases, Timescale and Influx, using data from Python scripts.
The Python scripts with the data to be visualized need to be in the same directory as this script.
First, it defines color codes for terminal output and metrics for the databases.
It then reads data from the Python scripts using the `read_data` and `read_data_load` functions.
The `parse_data` and `parse_data_load` functions are used to parse the data from the scripts.
These functions use regular expressions to find matches in the data and then format the matches into a more usable form.
The `print_table` and `print_table_load` functions are used to print the parsed data in a table format in the terminal.
The tables show the metrics for each database and each test, with the metrics color-coded based on their values.
The script then loops over different databases and metrics, parsing the data and printing it in table format.
The color codes for the metrics are switched based on the metric being processed.
The script is designed to be run from the command line and doesn't take any arguments.
"""
import ast
import re

red = '\033[91m'
green = '\033[93m'
blue = '\033[94m'
value_color = '\033[00m'
default = '\033[0m'

# For query table
def read_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    start_index = data.index('# small database\n') + 1
    data = ''.join(data[start_index:])
    return data

# For load table
def read_data_load(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    start_index = data.index('# worker1: [total_time, rows/s, metrics/s]\n') + 1
    data = ''.join(data[start_index:])
    return data

# For query table
def parse_data(data, database, col):
    parsed_data = {}
    for match in re.finditer(r'(' + database + '_\w+)\s+=\s+(\[\[.*?\]\])', data):
        test_name = match.group(1)
        test_data = ast.literal_eval(match.group(2))
        parsed_data[test_name] = {'1 Worker': test_data[0][col], '2 Workers': test_data[1][col], '4 Workers': test_data[2][col]}
    return parsed_data

# For load table
def parse_data_load(data, database, col):
    parsed_data = {}
    for match in re.finditer(r'(' + database + '_lo\w+)\s+=\s+(\[\[.*?\]\])', data):
        test_name = match.group(1)
        test_data = ast.literal_eval(match.group(2))
        parsed_data[test_name] = {'1 Worker': test_data[0][col], '2 Workers': test_data[1][col], '4 Workers': test_data[2][col], '8 Workers': test_data[3][col]}
    return parsed_data

# For query table
def print_table(influx_data, timescale_data, metric, new_green, new_red):
    print('\n' + ' ' * 36 + metric + ' per worker' + '\n')
    print('+--------------------------------+------------+-----------------+-----------------+-----------------+')
    print('| Query Type' + ' ' * 21 + '| Database' + ' ' * 3 + '| 1 Worker' + ' ' * 8 + '| 2 Workers' + ' ' * 7 + '| 4 Workers' + ' ' * 7 + '|')
    print('+--------------------------------+------------+-----------------+-----------------+-----------------+')
    for test_name in influx_data.keys():
        print('|', blue + test_name.ljust(30), default + '|', green + 'Influx'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers']:
            influx_val = influx_data[test_name][worker]
            timescale_val = timescale_data[test_name][worker]
            percentage = round(influx_val / timescale_val * 100)
            color_code = new_red if percentage > 100 else new_green
            print('|',(f"{value_color}{influx_val} {color_code}({percentage}%)").ljust(25) + default, end=' ')
        print('|')
        print('|', ''.ljust(30), '|', red + 'Timescale'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers']:
            timescale_val = timescale_data[test_name][worker]
            print('|', value_color + str(timescale_val).ljust(15) + default, end=' ')
        print('|')
        print('+--------------------------------+------------+-----------------+-----------------+-----------------+')

# For load table
def print_table_load(influx_data, timescale_data, metric, new_green, new_red):
    print('\n' + ' ' * 51 + metric + ' per worker' + '\n')
    print('+--------------------------------+------------+------------------+------------------+------------------+------------------+')
    print('| Load Type' + ' ' * 22 + '| Database' + ' ' * 3 + '| 1 Worker' + ' ' * 9 + '| 2 Workers' + ' ' * 8 + '| 4 Workers' + ' ' * 8 + '| 8 Workers' + ' ' * 8 + '|')
    print('+--------------------------------+------------+------------------+------------------+------------------+------------------+')
    for test_name in influx_data.keys():
        print('|', blue + test_name.ljust(30), default + '|', green + 'Influx'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers', '8 Workers']:
            influx_val = influx_data[test_name][worker]
            timescale_val = timescale_data[test_name][worker]
            percentage = round(influx_val / timescale_val * 100)
            color_code = new_red if percentage > 100 else new_green
            print('|',(f"{value_color}{influx_val} {color_code}({percentage}%)").ljust(26) + default, end=' ')
        print('|')
        print('|', ''.ljust(30), '|', red + 'Timescale'.ljust(10) + default, end=' ')
        for worker in ['1 Worker', '2 Workers', '4 Workers', '8 Workers']:
            timescale_val = timescale_data[test_name][worker]
            print('|', value_color + str(timescale_val).ljust(16) + default, end=' ')
        print('|')
        print('+--------------------------------+------------+------------------+------------------+------------------+------------------+')

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

timescale_data_load = read_data_load('timescale.py')
influx_data_load = read_data_load('influx.py')

metric_load = ['Total Time (s)', 'Rows per second', 'Metrics per second']
databases_load = ['small', 'medium', 'big']

for database in databases_load:
    for col in range(3):
        if col == 1 or col == 2:
            new_green = '\033[91m'
            new_red = '\033[93m'
        else:
            new_green = '\033[93m'
            new_red = '\033[91m'
        parsed_timescale_data_load = parse_data_load(timescale_data_load, database, col)
        parsed_influx_data_load = parse_data_load(influx_data_load, database, col)
        print_table_load(parsed_influx_data_load, parsed_timescale_data_load, metric_load[col], new_green, new_red)
