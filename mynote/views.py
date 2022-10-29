from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Course, Topic, Note
from .forms import Courseform, Topicform, Noteform

def ensure_is_user(item, request):
    """Ensures data is only accessible to current user"""
    if item.owner != request.user:
        raise Http404

def index(request):
    """Shows the homepage  for note4all"""
    return render(request, "mynote/index.html")

@login_required
def courses(request):
    """Show all courses."""
    courses = Course.objects.filter(owner=request.user).order_by('date_started')
    context = {'courses': courses}
    return render(request, 'mynote/course.html', context)

@login_required
def course(request, course_id):
    """Show a single course and all it's topics."""
    course = Course.objects.get(id=course_id)

    #making sure its only accessible to current user
    ensure_is_user(course, request)

    topics = course.topic_set.order_by('-date_started')
    context = {'course': course, 'topics': topics}
    return render(request, 'mynote/topic.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and it's notes."""
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date_started')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'mynote/note.html', context)

@login_required
def new_course(request):
    """Add a new course"""
    if request.method != 'POST':
        #creates a blank form
        form = Courseform()
    else:
        #process/POST submitted data
        form = Courseform(request.POST)
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.owner = request.user
            new_course.save()
            return HttpResponseRedirect(reverse('mynote:courses'))
    context = {'form': form}
    return render(request, 'mynote/new_course.html', context)

@login_required
def new_topic(request, course_id):
    """Add a new topic per course"""
    course = Course.objects.get(id=course_id)

    if request.method != 'POST':
        #creates a blank form
        form = Topicform()
    else:
        #process/POST submitted data
        form = Topicform(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.course = course
            new_topic.save()
            return HttpResponseRedirect(reverse('mynote:course',
                                        args=[course_id]))
    context = {'course': course, 'form': form}
    return render(request, 'mynote/new_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    """Edit a topic"""
    topic = Topic.objects.get(id=topic_id)
    course = topic.course

    ensure_is_user(topic, request)

    if request.method != 'POST':
        #initial request; pre-fill form with the current topic
        form = Topicform(instance=topic)
    else:
        #process/POST submitted data
        form = Topicform(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mynote:course',
                                        args=[topic_id]))
    context = {'topic': topic, 'course': course, 'form': form}
    return render(request, 'mynote/edit_topic.html', context)

@login_required
def new_note(request, topic_id):
    """Add new notes per topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #creates a blank form
        form = Noteform()
    else:
        #process/POST submitted data
        form = Noteform(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.topic = topic
            new_note.save()
            return HttpResponseRedirect(reverse('mynote:topic',
                                        args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'mynote/new_note.html', context)

@login_required
def edit_note(request, note_id):
    """Editing notes"""
    note = Note.objects.get(id=note_id)
    topic = note.topic

    ensure_is_user(note, request)

    if request.method != 'POST':
        #initial request; pre-fill form with the current note
        form = Noteform(instance=note)
    else:
        #process/POST submitted data
        form = Noteform(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mynote:topic',
                                        args=[note_id]))
    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'mynote/edit_note.html', context)
