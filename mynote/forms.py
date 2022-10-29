from django import forms
from .models import Course, Topic, Note


class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course']
        labels = {'text': ''}

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        labels = {'text': ''}

class Noteform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['notes']
        labels = {'text': ''}
        widgets = {'notes': forms.Textarea(attrs={'cols':80})}
