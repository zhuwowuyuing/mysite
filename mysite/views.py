#coding=utf-8

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def first_page(request):
	#return HttpResponse("<p>Welcome to the page at %s</p>" % request.get_host())
	ua = request.META.get('HTTP_USER_AGENT', 'unknown')
	return HttpResponse("Your browser is %s" %ua)

def current_datetime(request):
	current_date = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_datetime':now}))
	current_section = "hello"
	return render(request, 'mysite/current_datetime.html', locals())
#	return HttpResponse(html)



# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	html = "<html><body>It is now %s.</body></html>" % now
# 	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)	
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s,%s</td></tr>' % (k, str(v)))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

