import datetime
class Member:
    """docstring for Member. Every member has name and age. Can be edited"""
    def __init__(self, name, age):
        self.name = name
        self.id = 0
        self.age = age
        self.posts = []

    def __str__(self):
        return "\nName: {}\nAge: {}\n".format(self.name, self.age)

class Post:
    """docstring for Post."""
    def __init__(self, title, main_post,member_id=0):
        self.date = datetime.datetime.now()
        self.id = 0
        self.title = title
        self.main_post = main_post
        self.member_id = member_id
        print ("NEW POST!!\n")

    def __str__(self):
        return "POST\nWritten By: {}\nTitle: {}\nPost: {}\n".format(self.owner_name, self.title, self.main_post)
