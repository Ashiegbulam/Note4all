"""Defines urls patterns for note4all."""

# from django.conf.urls import url
from . import views
from django.urls import include, re_path

urlpatterns = [
    #homepage
    re_path(r'^$', views.index, name='index'),
    #courses page
    re_path(r'^course/$', views.courses, name='courses'),
    #topics of a course page
    re_path(r'^courses/(?P<course_id>\d+)/$', views.course, name='course'),
    #notes of a topic page
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #page for adding a new course
    re_path(r'^new_course/$', views.new_course, name='new_course'),
    #page for adding a new topic
    re_path(r'^new_topic/(?P<course_id>\d+)/$', views.new_topic, name='new_topic'),
    #page for editing a topic
    re_path(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    #page for adding new notes
    re_path(r'^new_note/(?P<topic_id>\d+)/$', views.new_note, name='new_note'),
    #page for editing notes
    re_path(r'^edit_note/(?P<note_id>\d+)/$', views.edit_note, name='edit_note'),

]