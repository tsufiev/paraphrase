# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib import admin

class Entry(models.Model):
    text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["id"]

class Article(Entry):
    title = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.title or u"Статья %s" % self.id

class Announcement(Entry):
    pass

class Contact(Entry):
    pass

class Video(Entry):
    url = models.URLField()

class Feedback(Entry):
    author = models.CharField(max_length=50)

admin.site.register(Article)
admin.site.register(Feedback)
admin.site.register(Announcement)
admin.site.register(Video)
admin.site.register(Contact)

