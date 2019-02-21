from django.db import models

class TodoItem(models.Model): #this creates a special class called TodoItem, this represents each Todo item in database 
    content = models.TextField()