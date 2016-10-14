import argparse
import shutil
import os

import yaml

from datetime import date
from string import Template

def generate_post_file(filename, title):
    """
    Create the post file.

    Keyword arguments:
    filename -- name of the file to be created
    title -- title of the post
    """

    print(" Generating post file...", end="")

    with open('post.template', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    t = Template(template_file_content)

    actual_file_content = t.substitute(post_title=title)

    with open(filename, 'w', encoding='utf-8') as actual_file:
        actual_file.write(actual_file_content)
    print(" done!")

def get_post_destination(config_filename):
    """
    Read the config yaml file, and return the filepath to the Jekyll
    folder that contains the posts.
    """

    with open(config_filename, 'r', encoding='utf-8') as config_file:
        doc = yaml.load(config_file)
    return doc['posts_location']

def make_filename(post_title, date_prefix):
    title_formatted = post_title.replace(' ', '-')
    filename = date_prefix + '-' + title_formatted + '.md'
    return filename

def get_current_date_prefix():
    """
    Return the date in the format: 'YEAR=MONTH-DAY'
    """

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

    post_title = args.title.strip() # remove whitespaces that may be at
                                    # either ends.
    filename = make_filename(post_title, get_current_date_prefix())
    print(" Post Title: ", post_title)
    print(" Filename: ", filename)

    generate_post_file(filename, post_title)

    try:
        post_destination = get_post_destination('jekpost_config.yaml')
        print(" Moving to: ", post_destination)
        shutil.move(src=filename, dst=post_destination)
    except Exception as e:
        print("\n", type(e).__name__, ": ", e)
        os.remove(filename)  # remove local copy of post file
    else:
        print("\n New post created!\n Happy blogging!")

if __name__ == '__main__':
    main()
