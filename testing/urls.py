from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sections/$', views.sections, name='sections'),
    url(r'^sections/(?P<alias_section>[^/]+)/$', views.tests),
    #url(r'^sections/(?P<alias_section>[^/]+)/(?P<alias_test>[^/]+)/(?P<alias_question>[^/]+)', views.questions),
    url(r'^sections/(?P<alias_section>[^/]+)/(?P<alias_test>[^/]+)/(?P<question_number>[^/]+)', views.question),

]