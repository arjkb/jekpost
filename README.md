<div class="wrapper">
  <header>
  Bar!
  </header>
</div>
# JekPost

JekPost is a simple script to ease the post creation ritual of Jekyll.

As of today, the script does the following:

* Create a new jekyll post file with appropriately formatted filename
* Add a basic YAML front matter block to the top of the post file.

## Installation

JekPost is written in python. You need python 3 to install and run it.

The easiest way to install jekpost is via `pip`:
```
pip install jekpost
```

### Post Creation

To create a new post, run:
```
jekpost 'My Awesome Post' dir
```

* `My Awesome Post` is the post title
* `dir` is where you want the post file to be; this is typically the `_posts` directory.
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

You should replace the excerpt, tags, and post content with values specific to your post.

If you use jekyll, try out JekPost. I could use some feedback!


#### Project Links
* JekPost on GitHub: [https://github.com/arjunkrishnababu96/jekpost](https://github.com/arjunkrishnababu96/jekpost)
* JekPost on PyPi: [https://pypi.python.org/pypi/JekPost](https://pypi.python.org/pypi/JekPost)

---
\* *it's 14 August 2017 at the time of writing this article*
