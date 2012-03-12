# -*- coding: utf-8 -*-
from models import *
from photologue.models import Gallery

sections = [
    {'id': 'home',
     'title': u'Плейбек театр "Парафраз"', 
     'model': Announcement,
     'objs_per_page': None},
    {'id':     'articles',
     'title': u'О плейбек театре', 
     'model': Article,
     'objs_per_page': None},
    {'id':     'announcements',
     'title': u'Афиша', 
     'model': Announcement,
     'objs_per_page': None},
    {'id':     'actors',
     'title': u'Актеры',
     'model': Actor,
     'objs_per_page': None},
    {'id':     'contacts',
     'title': u'Контакты',
     'model': Contact,
     'objs_per_page': None},
    {'id':     'photos',
     'title': u'Фотографии с перфомансов',
     'model': Gallery,
     'objs_per_page': 12},
    {'id':     'videos',
     'title': u'Видео с перфомансов',
     'model': Video,
     'objs_per_page': None},
    {'id':     'feedbacks',
     'title': u'Отзывы',
     'model': Feedback,
     'objs_per_page': None}]

def find_section(section_id):
    for section in sections:
        if section['id'] == section_id:
            return section
    return None

def get_section_ids():
    section_ids = []
    for section in sections:
        section_ids.append(section['id'])
    return section_ids
