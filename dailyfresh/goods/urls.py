from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^$',views.DetailView.as_view(),name='detail')

]
