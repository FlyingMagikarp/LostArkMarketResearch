import getopt
import sys
from datetime import datetime
from sys import argv


def add_data(item, value):
    time = get_time()
    date = get_date()
    day = get_day()
    row = build_csv_row(item, value, time, day, date)
    with open('data.csv', 'a') as fd:
        fd.write(row+'\n')

    print('Added row: ')
    print(row)


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def get_date():
    return datetime.today().strftime('%Y-%m-%d')


def get_day():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    day_nr = datetime.today().weekday()

    return days[day_nr]


def build_csv_row(item, value, time, day, date):
    return item + ',' + value + ',' + time + ',' + day + ',' + date


if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "i:v:")
    except:
        sys.exit("Error getting arguments")

    # check inputs
    item = ' '
    value = ' '
    for opt, arg in opts:
        if opt in ['-i']:
            item = arg
        elif opt in ['-v']:
            value = arg

    if str.isspace(item) or str.isspace(value):
        sys.exit("One or more arguments are empty")

    add_data(item, value)
