![Preview of post](https://raw.githubusercontent.com/sammarxz/04-instagram-post-generator/master/2020-08-04.png)

# 04-instagram-post-generator
ok, I confess that I wavered a few days and was unable to follow the right sequence, but let's try again right? 

In this project I created a Python script that will take quotes from a [website](https://www.codeofliving.com/blog/55-powerful-short-quotes-sayings-life/
), generate an image for each quote and then post one per day on Instagram.

The idea is to automate, making the computer automatically run this script every day and post a post.

## How to use
```
git clone git@github.com:sammarxz/04-instagram-post-generator.git
pip install -r requirements.txt
python app.py
```

To run this script you will need set **ENVIROMENTS VARIABLES**. You can do this creating a **.env** file with this content:

```
export INSTAGRAM_USERNAME='yourusername'
export INSTAGRAM_PASSWORD='password'
```
and run `source .env`

## Features
- PIL for create images with Python
- WEB SCRAPPING with Bs4
- Use instapy-cli

## ToDo
* [ ] - Create a bash script to run this program every day at 12:12 pm

---
#### Disclaimer
Right now the [instapy-cli](https://github.com/instagrambot/instapy-cli/issues/99) is having an error that is unable to post anything.
Reported by many users who [opened issues](https://github.com/instagrambot/instapy-cli/issues) too. 
