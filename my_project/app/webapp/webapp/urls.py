from django.conf.urls import patterns, include, url

from webapp.views import baojiabiao,baojia,instockbaby,jipiao, current_time,index,dr,hello, lljhb,llchb,xjjjhb,xjjchb,dealin,cgin,cginv,cgckb, My_Homepage_view#, search_papers

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'webapp.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^time/$',current_time),
    url(r'^admin/', include(admin.site.urls)),
	url('^dealin/$',dealin),
	url('^dr/$',dr),
	url('^cgin/$',cgin),
	url('^cgckb/$',cgckb),
        url('^cginv/$',cginv), 
	url('^lljhb/$',lljhb),
	url('^llchb/$',llchb),
	url('^xjjjhb/$',xjjjhb),
	url('^xjjchb/$',xjjchb),
		url('^xjjchb2/$',xjjchb),
		url('^jipiao/$',jipiao),
		url('^instockbaby/$',instockbaby),
			url('^baojia/$',baojia),
			url('^baojiabiao/$',baojiabiao),
 
)
