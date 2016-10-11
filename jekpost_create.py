import argparse
from datetime import date

def get_current_date():
    today = date.today()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    date_string = year + '-' + month + '-' + day
    return date_string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('title', help='Post title')
    args = parser.parse_args()
    post_title = args.title
    date_prefix = get_current_date()
    print(" Post Title: ", post_title)
    print(" Date Prefix: ", date_prefix)

if __name__ == '__main__':
    main()
