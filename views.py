from django.shortcuts import render_to_response, redirect

def home(request):
    return render_to_response('home.html')

def actors(request):
    return redirect('/photologue/gallery/actors')
