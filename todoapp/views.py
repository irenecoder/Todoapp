from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic,Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    #the homepage for todoapp
    return render(request,'todoapp/index.html')
@login_required
def topics(request):

    #show all topics
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics': topics}
    return render(request,'todoapp/topics.html',context)
@login_required
def topic(request,topic_id):
    #show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'todoapp/topic.html',context)
@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #No data submitted;create a blank form
        form = TopicForm()
    else:
        #POST data submitted;process data
        form = TopicForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:topics'))
    context = {'form':form}
    return render(request,'todoapp/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    #add a new entry for a particular topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #no data submitted create a blank  page
        form = EntryForm()
    else:
        #POST data submitted;process data
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('todoapp:topic',args=[topic_id]))

    context = {'topic':topic,'form':form}
    return render(request,'todoapp/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    #edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #initial request; process data
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:topic',args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'todoapp/edit_entry.html',context)