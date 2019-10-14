from mongoengine import *

connect('blogantastic')


# Create your models here.

class User(Document):
    username = StringField(max_length=20)
    password = StringField(max_length=20)


class Post(Document):
    title = StringField(max_length=50)
    text = MultiLineStringField()

