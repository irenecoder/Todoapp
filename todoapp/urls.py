#from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/',views.index, name='index'),
    path('topics/',views.topics,name='topics'),
    #page for adding new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #details page for a single topic
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #page for adding a new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #page for editing an entry
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]
