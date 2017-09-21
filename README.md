# JekPost

A simple script to ease the post creation ritual of [Jekyll.](https://jekyllrb.com/)

As of today, the script does the following:
1. Create a new jekyll post file with appropriately formatted filename.
2. Add required metadata to the top of the post file.

### Installation

JekPost is written in python. You need python 3 to install and run it.

The easiest way to install jekpost is via [`pip`](https://pypi.python.org/pypi/pip). From your terminal, run:
```
pip install jekpost
```

### Post Creation

To create a new post, run:
```
jekpost 'My Awesome Post' dir
```

* `My Awesome Post` is the post title
* `dir` is where you want the post file to be; typically the `_posts` directory.
* `2017-08-14-my-awesome-post.md`* would be created inside `dir` with the necessary headers.

There! That takes care of all the heavy lifting associated with creating a new jekyll post.

### Full Example

```
$ jekpost 'My Awesome Post' _posts
 Post Title: My Awesome Post
 New post created: 2017-08-14-my-awesome-post.md
$ cat _posts/2017-08-14-my-awesome-post.md
---
layout: post
title: My Awesome Post
excerpt: Your excerpt goes here
tags: tag1, tag2
---
Your post content goes here
```

Replace the excerpt, tags, and post content with values specific to your post.

If you use jekyll, try out JekPost. I could use some feedback!


### Project Links
* [JekPost on GitHub](https://github.com/arjunkrishnababu96/jekpost)
* [JekPost on PyPi](https://pypi.python.org/pypi/JekPost)
* [Download ZIP file](https://github.com/arjunkrishnababu96/jekpost/archive/master.zip)
* [My blog article about Jekyll](https://arjunkrishnababu96.github.io/introducing-jekpost/)

---
\* *it's 14 August 2017 at the time of writing this article*
