#!/usr/bin/env python3

import argparse
import shutil
import os

import yaml

from datetime import date
from string import Template

CONFIG_FILE_NAME = 'jekpost_config.yaml'

def read_template_file(template_file):
    """
    Read a template file, and return it as a Template object
    """

    with open(template_file, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def generate_post_file(filename, title, disqus_name=None):
    """
    Create the post file.

    Keyword arguments:
    filename -- name of the file to be created
    title -- title of the post
    """

    print(" Generating post file...", end="")

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)

    template_path = dname + '/templates/'

    # post_template = read_template_file('templates/post.template')
    post_template = read_template_file(template_path + 'post.template')
    actual_file_content = post_template.substitute(post_title=title)

    # if os.path.isfile(filename):
    #     print("Error: File already exists!")
    #     raise Exception(" EXC: File Already Exists!")

    with open(filename, 'w', encoding='utf-8') as actual_file:
        actual_file.write(actual_file_content)
        if disqus_name is not None:
            t = read_template_file(template_path + 'disqus.template')
            disqus_script = t.substitute(disqus_shortname=disqus_name)
            actual_file.write(disqus_script)
    print(" done!")

def read_config(config_filename, config_key):
    """
    Read the yaml config file, and return the config_key value
    """

    with open(config_filename, 'r', encoding='utf-8') as config_file:
        doc = yaml.load(config_file)

    if config_key in doc:
        return doc[config_key]
    else:
        print(" Could not find " + config_key + " in " + config_filename)
        return None

def make_filename(post_title, date_prefix):
    title_formatted = post_title.replace(' ', '-')
    filename = date_prefix + '-' + title_formatted + '.md'
    return filename

def get_current_date_prefix():
    """
    Return the date in the format: 'YEAR=MONTH-DAY'
    """

    today = date.today()
    return str(today.year) + '-' + str(today.month) + '-' + str(today.day)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('title', help='Post title')
    parser.add_argument('location', help='Destination directory')
    parser.add_argument('-dq', '--disqus', help='Disqus shortname')
    args = parser.parse_args()

    post_title = args.title.strip() # remove whitespaces that may be at
                                    # either ends.
    filename = make_filename(post_title, get_current_date_prefix())

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)

    print(" Disqus shortname: ", args.disqus)
    print(" Abspath: ", abspath)
    print(" Dirname: ", dname)
    print(" Post Title: ", post_title)
    print(" Filename: ", filename)

    try:
        if args.disqus:
            generate_post_file(filename, post_title, args.disqus)
        else:
            generate_post_file(filename, post_title)

        print(" Moving to: ", args.location)
        shutil.move(src=filename, dst=args.location)
    except Exception as e:
        # print("\n", type(e).__name__, ": ", e)
        print("\n ERROR:", e)
        print("\n Aborting!")
        os.remove(filename) # remove local copy of post file
    else:
        print("\n New post created!\n Happy blogging!")

if __name__ == '__main__':
    main()
