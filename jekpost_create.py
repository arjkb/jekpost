#!/usr/bin/env python3

import argparse
import shutil
import os

import yaml

from datetime import date
from string import Template

CONFIG_FILE_NAME = 'jekpost_config.yaml'

class FileGenerationError(Exception):
    pass

def read_template_file(template_file):
    """
    Read a template file, and return it as a Template object
    """

    with open(template_file, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# def generate_post_file(filename, title, disqus_name=None):
#     """
#     Create the post file.
#
#     Keyword arguments:
#     filename -- name of the file to be created
#     title -- title of the post
#     """
#
#     print(" Generating post file...", end="")
#
#     abspath = os.path.abspath(__file__)
#     dname = os.path.dirname(abspath)
#
#     # template_path = dname + '/templates/'
#     template_file_name = os.path.join(dname, "templates", "post.template")
#     disqus_file_name = os.path.join(dname, "templates", "disqus.template")
#
#     # post_template = read_template_file('templates/post.template')
#     # post_template = read_template_file(template_path + 'post.template')
#     post_template = read_template_file(template_file_name)
#     actual_file_content = post_template.substitute(post_title=title)
#
#     if os.path.isfile(filename):
#         raise FileGenerationError("File already exists in current directory")
#
#     with open(filename, 'w', encoding='utf-8') as actual_file:
#         actual_file.write(actual_file_content)
#         if disqus_name is not None:
#             # t = read_template_file(template_path + 'disqus.template')
#             t = read_template_file(disqus_file_name)
#             disqus_script = t.substitute(disqus_shortname=disqus_name)
#             actual_file.write(disqus_script)
#     print(" done!")

def generate_post_file(title, location, disqus_name=None):

    print(" Generating post file...", end="")
    filename = make_filename(title, get_current_date_prefix())

    src_path = os.path.abspath(__file__)
    src_dir = os.path.dirname(src_path)

    template_dir = os.path.join(src_dir, "templates")
    post_template_path = os.path.join(template_dir, "post.template")
    disqus_template_path = os.path.join(template_dir, "disqus_template")

    post_template = read_template_file(post_template_path)
    actual_file_content = post_template.substitute(post_title=title)

    os.chdir(location) # switch to destination directory

    with open(filename, 'x', encoding='utf-8') as actual_file:
        actual_file.write(actual_file_content)
        if disqus_name is not None:
            t = read_template_file(disqus_template_path)
            disqus_script = t.substitute(disqus_shortname=disqus_name)
            actual_file.write(disqus_script)

    print(" done!")
    return filename

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
    # filename = make_filename(post_title, get_current_date_prefix())

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)

    print(" Disqus shortname: ", args.disqus)
    print(" Abspath: ", abspath)
    print(" Dirname: ", dname)
    print(" Post Title: ", post_title)
    # print(" Filename: ", filename)

    # try:
    #     filename = generate_post_file(post_title, args.location, args.disqus)
    #     # if args.disqus:
    #         # filename = generate_post_file(post_title, args.location, args.disqus)
    #     # else:
    #     #     generate_post_file(filename, post_title)
    #
    #     if args.location is not '.':
    #         print(" Moving to: ", args.location)
    #         shutil.move(src=filename, dst=args.location)
    #
    # except FileGenerationError as err:
    #     print("\n\n Error: ", err)
    #     print(" Remove similarly named file in current directory and retry.")
    # except shutil.Error as err:
    #     # print("\n", type(e).__name__, ": ", e)
    #     print("\n Error: ", err)
    #     os.remove(filename) # remove local copy of post file
    # else:
    #     print("\n New post created!\n Happy blogging!")

    try:
        filename = generate_post_file(post_title, args.location, args.disqus)
    except FileExistsError as err:
        print("\n\n", err)
    except FileNotFoundError as err:
        print("\n\n", err)
    except NotADirectoryError as err:
        print("\n\n", err)
    else:
        print(" New post created: ", filename)
        print(" Happy blogging!")

if __name__ == '__main__':
    main()
