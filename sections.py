# -*- coding: utf-8 -*-
from articles.models import *

sections = [
    {'id': 'home',
     'title': u'Плейбек театр "Парафраз"', 
     'model': None},
    {'id':     'theory',
     'title': u'О плейбек театре', 
     'model': Article},
    {'id':     'upcoming',
     'title': u'Афиша', 
     'model': Announcement},
    {'id':     'actors',
     'title': u'Актеры',
     'model': None},
    {'id':     'contacts',
     'title': u'Контакты',
     'model': Contact},
    {'id':     'photos',
     'title': u'Фотографии с перфомансов',
     'model': None},
    {'id':     'video',
     'title': u'Видео с перфомансов',
     'model': Video},
    {'id':     'feedback',
     'title': u'Отзывы',
     'model': Feedback}]

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
