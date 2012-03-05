# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib import admin

class Entry(models.Model):
    text = models.TextField(u'Текст')
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

def cut_text(text):
    if len(text) < 20:
        return text
    else:
        return u'%s...'%text[0:50]

class Announcement(Entry):
    def __unicode__(self):
        return cut_text(self.text)

class Contact(Entry):
    def __unicode__(self):
        return cut_text(self.text)

class Video(Entry):
    url = models.URLField()
    def __unicode__(self):
        return cut_text(self.text)

class Feedback(Entry):
    author = models.CharField(u'Автор',max_length=50)
    def __unicode__(self):
        timestamp = self.published_on.strftime('%d.%m.%Y %H:%M')
        return u'Отзыв от %s, автор: %s'% (timestamp, self.author)

class TitledEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Article, TitledEntryAdmin)
admin.site.register(Announcement)
admin.site.register(Actor, TitledEntryAdmin)
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(Feedback)
