class Member:
    """docstring for Member. Every member has name and age. Can be edited"""
    def __init__(self, mem_id, name, age):
        self.__id = mem_id
        self._name = name
        self._age = age
        self.__posts = {}

    def __str__(self):
        return "\nName: {}\nAge: {}\n".format(self._name, self._age)

    def edit_name(self, new_name):
        self._name = new_name

    def edit_age(self, new_age):
        self._age = new_age

    def get_posts(self):
        return self.__posts

    def new_post(self, post_id, title, main_post):
        self.__posts[post_id] = Post(post_id, self.__id, self._name, title, main_post)
        return self.__posts[post_id]

    def del_post(self, post_id, post):
        if post_id in self.__posts.keys():
            del self.__posts[post_id]
            del post
            print "Delete Successful!\n"
        else:
            print "You Can't delete this post.\n"



class Post:
    """docstring for Post."""
    def __init__(self, post_id, owner_id, owner_name, title, main_post):
        self.__post_id = post_id
        self._owner_id = owner_id
        self._owner_name = owner_name
        self._title = title
        self._main_post = main_post
        print "NEW POST!!\n"

    def __str__(self):
        return "POST\nWritten By: {}\nTitle: {}\nPost: {}\n".format(self._owner_name, self._title, self._main_post)

    def get_id(self):
        return self.__post_id

    def edit_post(self, member, new_title, new_post):
        if member != self._owner_id:
            print "You are not the owner of this post. You can't edit it.\n"
            return

        self._main_post = new_post
        self._title = new_title
        print "Edit Successful!\n"
