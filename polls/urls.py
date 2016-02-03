from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^insertar/$', views.insertar, name='insertar'),
    url(r'^actualizar/$', views.actualizar, name='actualizar'),
    url(r'^borrar/$', views.borrar, name='borrar'),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
    url(r'^ejemplo1/$', views.ejemplo1),
    url(r'^ejemplo2/$', views.ejemplo2),
    url(r'^ejemplo3/$', views.ejemplo3),
    url(r'^lista_borrar/$', views.lista_borrar, name='lista_borrar'),
    url(r'^borrar2/$', views.borrar2, name='borrar2'),
]