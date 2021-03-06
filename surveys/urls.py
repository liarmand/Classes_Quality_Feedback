from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^(?P<a>\d+)/(?P<b>\d+)/$',  views.summ, name='sum'),
    url(r'^(?P<id>\d+)/survey_result/$',  views.survey_result, name='survey_result'),
    url(r'^(?P<id>\d+)/survey_submit/$',  views.survey_submit, name='survey_submit'),
    url(r'^(?P<id>\d+)/survey_detail/$',  views.survey_detail, name='survey_detail'),
    url(r'^(?P<s_id>\d+)/survey_detail/(?P<q_id>\d+)/delete$',  views.question_delete, name='question_delete'),
    url(r'create_data/',  views.data_create, name='create_data'),
    path('survey_list/',  views.survey_list, name='survey_list'),
    path('', views.index, name='index')
]

