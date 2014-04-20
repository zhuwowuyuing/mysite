from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from books.views import about_pages

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.first_page'),
    url(r'^west/', include('west.urls')),
    url(r'^time/$', 'mysite.views.current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'mysite.views.hours_ahead'),
    url(r'^display/$', 'mysite.views.display_meta'),
    #url(r'^search-form/$', 'books.views.search_form'),
    url(r'^search/$', 'books.views.search'),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^contact/thanks/$', 'contact.views.thanks'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^about/(\w+)/$', about_pages),
)

