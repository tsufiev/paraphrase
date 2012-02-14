from django.shortcuts import render_to_response, redirect
from paraphrase.articles.models import Article

from paraphrase.sections import sections, titles
def show_section(request, section = 'home'):
    context = {'sections': sections,
               'title': titles[section],
               'current_section': section,
               'articles': Article.objects.filter(section=section)}
    return render_to_response('%s.html' % section, context)

def home(request):
    return render_to_response('home.html')

def actors(request):
    return redirect('/photologue/gallery/actors')

# sections = ['home', 'theory', 'upcoming', 'actors', 'contacts', 'photo', 
#             'video', 'feedback']

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
