---
layout: post
title: Hello World! Greetings, and a small tutorial to create a blog like this
excerpt: "How to create a static website+blog with Github, Jekyll, and a custom domain"
modified: 2/29/2016, 9:00:24
tags: [intro, beginner, jekyll, github, tutorial]
comments: false
category: blog
---

Hi there! My name is [Paulo](https://pregis.me/) and I'm a Ph.D. candidate at the University of Nevada, Reno. This is my website, here you can find my [academic work](https://pregis.me/publications), [curriculum](https://pregis.me/resume), and this blog!

Since this is the first post, and I want it to be useful, not a simple diary, I'll be posting quick and easy how-tos. To start things off I'll tell you how to create a similar website for yourself.

## What is Jekyll

Jekyll is a static site generator. If you don't need a full fledged content management system like wordpress, but rather just need a simple website with not many colaborators, Jekyll is your friend. 

## Choosing a Jekyll theme

Jekyl itself has a ton of different themes. Depending on your goals you might choose a different one. In my case, I looked for academic themes, the ones that emphasize on publications, teaching, CV, etc. A good resource to start is google itself, simply try "academic jekyll theme" or something similar. You can try [JekyllThemes.org](http://jekyllthemes.org/), but as of now, they don't have a search option.

After a week trying to find a simple one, I decided to go with the [Jekyll Academic](https://ncsu-libraries.github.io/jekyll-academic-docs/) template.

## Creating the github repository (aka repo) and copying template files

If you're not familiar with [github](https://github.com), don't worry. All you have to do is create an account (it's free), and a repo. For this purpose, you only need a free account, but if you pay, or have access to a .edu email account, you can create private repo, but that's a subject for another post. After you created your account, you have to copy the template contents to a very specific repo.

On the top right corner of your github account, click on the `+` button and create a `New Repository`. Now this is __very__ important: your repository has to be named __*your-github-username*.github.io__. Let it be public, and do **not** initialize with a README file.

![Creating a new repo]({{ "/images/blog/create-github-repo.png" | absolute_url }})

After hitting `Create` you'll be presented with various options to import content into your repo. In our case, let's import the content from another repo by clicking `Import code` at the bottom of the page.

![Import repo]({{ "/images/blog/import-code-github-repo.png" | absolute_url }})

Then we paste the link from our newly found theme, paste the link of your template, and click `Begin import`, and then wait a few minutes, you'll be notified when it finishes (you'll get an email, you can close the site):

![Begin importing repo]({{ "/images/blog/begin-import-github.png" | absolute_url }})

Great! Now if you open a new browser window/tab, and enter the link __*your-github-username*.github.io__, you should see the website up and running! Of course, the content has to be edited (in another post! Or you can check the [theme's documentation](https://ncsu-libraries.github.io/jekyll-academic-docs/) if you feel impatient).

## TravisCI

[TravisCI](https://travis-ci.org/) is a continuous integration service. What does it mean? Well, you know if you create a program in C/C++ you have to compile before you actually run it? It's kind of like that. Creating the website using Jekyll results in a bunch of files of different formats (.md, .yml, ...). The way you "compile" it to be visible in a web browser is using `bundler`.

If you want to test locally (a good idea to check there are no typos, errors, etc.), you simply go to your terminal, `cd /your/website/path`, and `bundler exec jekyll serve`. This will "compile" and serve your website locally, so you can go to your browser and check if the website is working. If you want to simply compile and create the files you need to upload to your server: `bundler exec jekyll build`. Then you have to upload the files yourself.

Travis helps you in automating this "build and serve" process. Everytime you update the files on GitHub, travis will run the `bundler exec jekyll build`, and copy the files to the right place. To enable your project to have travis, create the file `.travis.yml` (yes, with the period at the beginning). Inside the file, copy and paste the following:

    language: ruby
    rvm:
    - 2.2
    script: "bundle exec jekyll build"

Update (aka push) this change to your github repo. Now go to [Travis website](https://travis-ci.org/) and create an account using your GitHub account. Go ahead and add a repo to your travis account (plus sign, top-ish left). It should list all the repositories you have on github. Select the `user.github.io` repo. That's it! You should see the compiling logs on travis.

Now everytime you update your repo on github (add post, edit bio, etc.), Travis will automatically compile and copy the files!