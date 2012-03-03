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

class TitledEntry(Entry):
    title = models.CharField(max_length=100)
    title_slug = models.SlugField(unique=True)
    def __unicode__(self):
        return self.title

class Article(TitledEntry):
    pass

from photologue.models import Photo
class Actor(Photo):
    pass

class Announcement(Entry):
    pass

class Contact(Entry):
    pass

class Video(Entry):
    url = models.URLField()

class Feedback(Entry):
    author = models.CharField(max_length=50)

class TitledEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Article, TitledEntryAdmin)
admin.site.register(Announcement)
admin.site.register(Actor, TitledEntryAdmin)
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(Feedback)
