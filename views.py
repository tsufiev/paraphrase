from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from photologue.models import Photo, Gallery

from paraphrase.sections import sections, titles
from paraphrase.articles.models import Article

from math import ceil
def paginate_queryset(queryset, page, objs_per_page = 18):
    def div(a, b):
        return int(ceil(a / float(b)))
    if page:
        page, n = int(page), objs_per_page
        return queryset[ (page-1)*n : page*n ], div(len(queryset), n)
    else:
        return queryset, None

def show_section(request, section = 'home', template = None, context = {}):
    context = dict({'sections': sections,
                    'title': titles[section],
                    'current_section': section,
                    'articles': Article.objects.filter(section=section),
                    }.items() + context.items())
    return render_to_response(template or '%s.html'%section, context)

def show_photo(request, gallery, actor = None, photo = None):
    if actor:
        actor = get_object_or_404(Photo, title_slug=actor)
        return show_section(request, 'actors', 'photo.html', {'actor': actor})
    elif photo:
        photo = get_object_or_404(Photo, title_slug=photo)
        return show_section(request, 'photos', 'photo.html', {'photo': photo})
    else:
        raise Http404

from django.http import HttpResponse
    
def show_gallery(request, slug = 'actors', page = None):
    if slug:
        try:
            gallery = Gallery.objects.get(title_slug=slug)
        except ObjectDoesNotExist:
            raise Http404
        photos = gallery.photos.all()
        if slug != 'actors':
            photos = photos.order_by('id')
        objects, pages = paginate_queryset(photos, page)
    else:
        galleries = Gallery.objects.exclude(title_slug='actors')
        objects, pages = paginate_queryset(galleries, page)
    context = {'objects': objects, 
               'current_page': page,
               'current_gallery': slug,
               'pages': pages,
               }
    if slug == 'actors':
        return show_section(request, 'actors', 'gallery.html', context)
    else:
        # return HttpResponse('title %s, url %s' % (objects[0].title_slug, objects[0].))
        return show_section(request, 'photos', 'gallery.html', context)

        
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
