# -*- coding: utf-8 -*-

sections = [
    {'id': 'home',
     'title': u'Плейбек театр "Парафраз"', 
     'has_feed': False},
    {'id':     'theory',
     'title': u'О плейбек театре', 
     'has_feed': True},
    {'id':     'upcoming',
     'title': u'Афиша', 
     'has_feed': True},
    {'id':     'actors',
     'title': u'Актеры',
     'has_feed': False},
    {'id':     'actor',
     'title': u'Актеры',
     'has_feed': False},
    {'id':     'contacts',
     'title': u'Контакты',
     'has_feed': True},
    {'id':     'photo',
     'title': u'Фотографии с перфомансов',
     'has_feed': False},
    {'id':     'video',
     'title': u'Видео с перфомансов',
     'has_feed': False},
    {'id':     'feedback',
     'title': u'Отзывы',
     'has_feed': True}]

mappings = {'actor': 'actors'}
titles = dict([(entry['id'], entry['title']) for entry in sections])
text_sections = tuple([(section['id'], section['title'])
                       for section in sections if section['has_feed']])
