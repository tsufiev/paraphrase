from django.shortcuts import render_to_response, redirect
from paraphrase.articles.models import Article
from photologue.models import Photo, Gallery

from paraphrase.sections import sections, titles, mappings
def show_section(request, section = 'home'):
    context = {'sections': sections,
               'title': titles[section],
               'current_section': section,
               'articles': Article.objects.filter(section=section),
               'actors': Gallery.objects.get(title_slug='actors').photos.all(),
               'galleries': Gallery.objects.all()
               }
    return render_to_response('%s.html' % section, context)

def show_actor(request, actor):
    context = {'sections': sections,
               'title': titles['actors'],
               'current_section': 'actors',
               'actor': Photo.objects.get(title_slug=actor)
               }
    return render_to_response('actor.html', context)

def show_gallery(request, gallery, photo_id):
    context = {'sections': sections,
               'title': titles['photo'],
               'current_section': 'photo',
               'gallery': gallery,
               }
    if photo_id:
        context['photo'] = Photo.objects.get(id=photo_id)
    else:
        context['photos'] = Gallery.objects.get(title_slug=gallery).photos.all()
    return render_to_response('gallery.html', context)
    

# from os.path import basename
# import re
# def extract_fnum(path):
#     m = re.match(r'([0-9]{2})\.gif', basename(path))
#     if m:
#         return int(m.group(1))

# def rename_files(base):
#     for file in listdir(base):
#         n = extract_fnum(file)
#         if n:
#             rename(os.path.join(base,file), os.path.join(base,"%s.gif" % sections[n-1]))
