from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    """Course subject the user is taking."""
    course = models.CharField(max_length=100)
    date_started = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.course

class Topic(models.Model):
    """Topic the user is learning."""
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    date_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.topic

class Note(models.Model):
    """Notes about a topic"""
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    date_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        if len(self.notes) > 250:
            displaynotes = self.notes[:100] + "..."
        else:
            displaynotes = self.notes
        return displaynotes