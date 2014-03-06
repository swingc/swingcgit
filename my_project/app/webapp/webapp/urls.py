from django.conf.urls import patterns, include, url

from webapp.views import index,hello, lljhb,llchb,xjjjhb,xjjchb,dealin,cgin,cginv,cgckb, My_Homepage_view#, search_papers

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url('^dealin/',dealin),
	url('^cgin/',cgin),
	url('^cgckb/',cgckb),
        url('^cginv/',cginv), 
	url('^lljhb/',lljhb),
	url('^llchb/',llchb),
	url('^xjjjhb/',xjjjhb),
	url('^xjjchb/',xjjchb),
		url('^xjjchb2/',xjjchb),
 
)
