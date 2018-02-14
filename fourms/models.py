class Member:
    """docstring for Member. Every member has name and age. Can be edited"""
    def __init__(self, id, name, age):
        self._name = name
        self._id = id
        self._age = age
        self._posts = {}

    def __str__(self):
        return "\nName: {}\nAge: {}\n".format(self._name, self._age)

class Post:
    """docstring for Post."""
    def __init__(self, post_id, title, main_post):
        self._id = post_id
        self._title = title
        self._main_post = main_post
        print "NEW POST!!\n"

    def __str__(self):
        return "POST\nWritten By: {}\nTitle: {}\nPost: {}\n".format(self._owner_name, self._title, self._main_post)
