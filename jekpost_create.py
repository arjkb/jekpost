import argparse
import yaml
import shutil
from datetime import date
from string import Template

def copy_to_dest(filename, destination):
    shutil.copy(filename, destination)

def generate_post_file(filename, title):
    """
    Create the post file.

    Keyword arguments:
    filename -- name of the file to be created
    title -- title of the post
    """

    with open('post.template', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    t = Template(template_file_content)

    actual_file_content = t.substitute(post_title=title)

    with open(filename, 'w', encoding='utf-8') as actual_file:
        actual_file.write(actual_file_content)

def read_post_path(config_filename):
    """
    Read the config yaml file, and return the filepath to the Jekyll
    folder that contains the posts
    """

    with open(config_filename, 'r', encoding='utf-8') as config_file:
        doc = yaml.load(config_file)
    return doc['posts_location']

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
    generate_post_file(filename=filename, title=post_title)

    p = read_post_path('jekpost_config.yaml')
    print(p)
    copy_to_dest(filename, p)

if __name__ == '__main__':
    main()
