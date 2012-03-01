from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from photologue.models import Photo, Gallery

from paraphrase.sections import sections, titles
from paraphrase.articles.models import Article

OBJS_PER_PAGE = 6

from math import ceil
def paginate_queryset(queryset, page, objs_per_page = OBJS_PER_PAGE):
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

def show_photo(request, photo, gallery = 'actors'):
    if gallery == 'actors':
        section = 'actors'
    else:
        section = 'photos'
    return show_section(request, section, 'photo.html', 
                        {'photo': get_object_or_404(Photo, title_slug=photo)})

from django.core.paginator import Paginator
    
def show_gallery(request, slug = 'actors', page = None):
    if slug:
        gallery = get_object_or_404(Gallery, title_slug=slug)
        photos = gallery.photos.all()
        if slug == 'actors':
            return show_section(request, 'actors',
                                context = {'objects': photos, 
                                           'current_gallery': 'actors'})
        else:
            paginator = Paginator(photos.order_by('id'), OBJS_PER_PAGE)
    else:
        galleries = Gallery.objects.exclude(title_slug='actors')
        paginator = Paginator(galleries, OBJS_PER_PAGE)
    return show_section(request, 'photos', 'gallery.html', 
                        {'objects': paginator.page(int(page)),
                         'current_gallery': slug})

