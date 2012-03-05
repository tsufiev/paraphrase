from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect

from photologue.models import Photo, Gallery

from sections.views import find_section, get_section_ids
from sections.models import Feedback

OBJS_PER_PAGE = 6

def show_section(request, section_id = 'home', template = None, context = {}):
    section = find_section(section_id)
    model = section['model']
    context = dict({'sections': get_section_ids(),
                    'title': section['title'],
                    'current_section': section_id,
                    'entries': model and model.objects.all(),
                    }.items() + context.items())
    context.update(csrf(request))
    return render_to_response(template or '%s.html'%section_id, context)

from django.forms import ModelForm
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('author', 'text')

from django.core.context_processors import csrf
from django.template import RequestContext

def render_page(request, template, context):
    return render_to_response(template, context, 
                              context_instance = RequestContext(request))

def show_feedbacks(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedbacks/')
    else:
        form = FeedbackForm()
    return show_section(request, 'feedbacks', context = {'form': form})

from django.core.paginator import Paginator, EmptyPage

def show_photo(request, photo, gallery = None):
    photo = get_object_or_404(Photo, title_slug=photo)
    if gallery is None:
        return show_section(request, 'actors', 'photo.html', {
                'photo': photo})
    else:
        gallery_obj = Gallery.objects.get(title_slug=gallery)
        return show_section(request, 'photos', 'photo.html', {
            'photo': photo,
            'gallery': gallery,
            'page_number': get_gallery_page_number(gallery_obj, photo),
            'next_in_gallery': photo.get_next_in_gallery(gallery_obj),
            'prev_in_gallery': photo.get_previous_in_gallery(gallery_obj), 
            })
        
def make_pages(objs):
    return Paginator(objs, OBJS_PER_PAGE)

def get_page_number(paginator, object):
    for page in paginator.page_range:
        if object in paginator.page(page).object_list:
            return page

def get_gallery_page_number(gallery, photo):
        return get_page_number(make_pages(gallery.photos.order_by('id')), photo)

def show_gallery(request, slug = None, page = None):
    if slug:
        gallery = get_object_or_404(Gallery, title_slug=slug)
        paginator = make_pages(gallery.photos.order_by('id'))
    else:
        paginator = make_pages(Gallery.objects.all())
    try:
        return show_section(request, 'photos', 'gallery.html', 
                            {'objects': paginator.page(int(page)),
                             'current_gallery': slug})
    except EmptyPage:
        raise Http404
