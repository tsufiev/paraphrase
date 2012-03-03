from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from photologue.models import Photo, Gallery

from sections.views import find_section, get_section_ids

OBJS_PER_PAGE = 6

def show_section(request, section_id = 'home', template = None, context = {}):
    section = find_section(section_id)
    model = section['model']
    context = dict({'sections': get_section_ids(),
                    'title': section['title'],
                    'current_section': section_id,
                    'entries': model and model.objects.all(),
                    }.items() + context.items())
    return render_to_response(template or '%s.html'%section_id, context)

def show_photo(request, photo, gallery = 'actors'):
    section = 'actors' if gallery == 'actors' else 'photos'
    return show_section(request, section, 'photo.html', 
                        {'photo': get_object_or_404(Photo, title_slug=photo)})

from django.core.paginator import Paginator
    
def show_gallery(request, slug = 'actors', page = None):
    if slug:
        gallery = get_object_or_404(Gallery, title_slug=slug)
        paginator = Paginator(gallery.photos.order_by('id'), 
                              OBJS_PER_PAGE)
    else:
        paginator = Paginator(Gallery.objects.all(), OBJS_PER_PAGE)
    return show_section(request, 'photos', 'gallery.html', 
                        {'objects': paginator.page(int(page)),
                         'current_gallery': slug})

