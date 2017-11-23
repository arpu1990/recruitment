from django.conf.urls import include, url
from django.contrib import admin
import application.views as application_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'recruitment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),url(r'^dashboard/', 'application.views.dashboard'),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', application_view.application_form, name='application'),
    url(r'^admin/', application_view.admin, name='admin'),
    url(r'^dashboard/', application_view.dashboard, name='dashboard'),
    url(r'^users/(?P<status>[\w-]+)/$', application_view.users, name='users'),
    url(r'^user/(?P<user_id>[\d]+)/$', application_view.user, name='user'),
    url(r'^update_status/$', application_view.update_status, name='update_status'),
    url(r'^logout/$', application_view.logout, name='logout'),

]

