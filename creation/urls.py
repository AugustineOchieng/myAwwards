  
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='index'),
    url(r'^profile/(\d+)', views.profile, name='profile'),

    url(r'^new_profile/$',views.new_profile,name = 'NewProfile'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^new/project/$', views.new_project, name='new_post'),
    url(r'^single/new_comment/(\d+)/', views.new_comment, name='new_comment'),
    url(r'^comment/$',views.comment,name = 'comments'),
    
    url(r'^single/(\d+)', views.single, name='one_project'),
    url(r'^voter/$', views.voter, name='voting'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.Profilel.as_view()),
    url(r'^api/project/$', views.Projecter.as_view())
    
    # url(r'^image/(\d+)',views.image,name ='image'),
  ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)