import argparse
from datetime import date

def get_filename(post_title, date_prefix):
    title_formatted = post_title.replace(' ', '-')
    filename = date_prefix + '-' + title_formatted + '.md'
    return filename

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
    post_title = args.title.strip()
    date_prefix = get_current_date()
    filename = get_filename(post_title=post_title, date_prefix=date_prefix)
    print(" Post Title: ", post_title)
    print(" Date Prefix: ", date_prefix)
    print(" Filename: ", filename)

if __name__ == '__main__':
    main()
