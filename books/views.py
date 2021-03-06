from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

# Create your views here.

def search_form(request):
	return render(request,'books/search_form.html')

def search(request):
#if 'q' in request.GET and request.GET['q']:
#	q = request.GET['q']
#	books = Book.objects.filter(title__icontains=q)
#	return render(request,'books/search_results.html', {'books':books, 'query':q})
#else:
#	#return HttpResponse('Please submit a search term.')
#	return render(request,'books/search_form.html', {'error':True})
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books':books, 'query':q})
    return render(request, 'books/search_form.html', {'errors':errors})

def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s,html" % page)
    except TemplateDoesNotExist:
        raise Http404()