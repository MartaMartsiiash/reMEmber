"""
Forms for creating and editing diary notes.
"""


from django import forms
from .models import Note, Song, Mood


class NoteForm(forms.ModelForm):
    """
    Form for creating and editing notes.
    """
    song_title = forms.CharField(label="Назва пісні", max_length=150, required=False)
    song_artist = forms.CharField(label="Виконавець", max_length=150, required=False)
    song_url = forms.URLField(label="Посилання на пісню", required=False)
    mood = forms.ModelChoiceField(
        queryset=Mood.objects.all(),
        label="Твій настрій",
        empty_label="Оберіть настрій",
        widget=forms.Select(attrs={'class': 'mood-select'})
    )

    class Meta:
        """
        Metadata for NoteForm.
        """
        model = Note
        fields = ('text', 'mood', 'is_public')
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Що сьогодні сталося?', 'rows': 5}),
            'is_public': forms.CheckboxInput(),
        }
        labels = {
            'text': 'Текст нотатки',
            'is_public': 'Зробити нотатку публічною?',
        }

    def save(self, commit=True):
        """
        Save the note instance and optionally attach a song.
        """
        note = super().save(commit=False)
        s_title = self.cleaned_data.get('song_title')
        s_artist = self.cleaned_data.get('song_artist')
        s_url = self.cleaned_data.get('song_url')
        if s_title and s_url:
            song, created = Song.objects.get_or_create(
                title=s_title,
                artist=s_artist,
                url=s_url
            )
            note.song = song
        if commit:
            note.save()
        return note

    def clean(self):
        """
        Validate song fields consistency.
        """
        cleaned_data = super().clean()
        title = cleaned_data.get("song_title")
        url = cleaned_data.get("song_url")
        if title and not url:
            self.add_error("song_url", "Додайте посилання на пісню")
        if url and not title:
            self.add_error("song_title", "Додайте назву пісні")
        return cleaned_data
