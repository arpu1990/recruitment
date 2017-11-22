from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'recruitment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),url(r'^dashboard/', 'application.views.dashboard'),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'application.views.application_form'),
    url(r'^admin/', 'application.views.admin'),
    url(r'^dashboard/', 'application.views.dashboard'),
    url(r'^users/(?P<status>[\w-]+)/$', 'application.views.users'),
    url(r'^user/(?P<user_id>[\d]+)/$', 'application.views.user'),
    url(r'^update_status/$', 'application.views.update_status'),
    url(r'^logout/$', 'application.views.logout'),

]

