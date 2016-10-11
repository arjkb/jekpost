import argparse

parser = argparse.ArgumentParser()
parser.add_argument('title', help='Post title')
args = parser.parse_args()
post_title = args.title
print(" Post Title: ", post_title)
