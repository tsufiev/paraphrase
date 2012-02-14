# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.contrib import admin
from paraphrase.sections import text_sections

ordering_key_step = 10

class Article(models.Model):
    # def __init__(self):
    #     models.Model.__init__(self)
    #     articles = Article.objects.filter(section=self.section)
    #     if len(articles) > 1:
    #         ordering_key = articles[0].ordering_key + ordering_key_step
    #     else:
    #         ordering_key = 0;

    title = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=10, choices=text_sections)
    text = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)
    # ordering_key = models.IntegerField(null=True)

    def __unicode__(self):
        return u"[%s] %s" % (self.section, self.title or u"Статья")

    class Meta:
        ordering = ["id"]

# class ArticleAdmin(admin.ModelAdmin):
#     def add_view(self, request, form_url='', extra_context=None):
#         exclude = ('ordering_key',)
#         return super(ArticleAdmin, self).add_view(request)

#admin.site.register(Article, ArticleAdmin)
admin.site.register(Article)
