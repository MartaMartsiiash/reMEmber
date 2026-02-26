"""
Database models for notes, moods, songs, and quotes.
"""


from django.db import models
from django.conf import settings


class Mood(models.Model):
    """
    Represents a mood or emotional state.
    """

    name = models.CharField(max_length=150)
    emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        """
        Return a human-readable string representation of the mood.
        """
        return f"{self.name}{self.emoji}" if self.emoji else self.name

class Song(models.Model):
    """
    Represents a song associated with a note.
    """

    title = models.CharField(max_length=150, blank=True)
    artist = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a human-readable string representation of the song.
        """
        return f"{self.artist} - {self.title}"

class Quote(models.Model):
    """
    Represents a short quote.
    """
    text = models.TextField()

    def __str__(self):
        """
        Return a human-readable string representation of the quote.
        """
        return self.text

class Note(models.Model):
    """
    Represents a user-created note.
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notes'
    )
    text = models.TextField(max_length=3000)
    mood = models.ForeignKey(
        Mood,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notes'
    )
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_notes',
        blank=True
    )

    def __str__(self):
        """
        Return a human-readable string representation of the note.
        """
        name = self.author.username if self.author else "Невідомий автор"
        privacy = "Публічний" if self.is_public else "Приватний"
        return f"{name} | {privacy} | {self.created_at.date()}"
