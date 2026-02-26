"""
Views for diary application.
"""


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Note, Quote, Song
from .forms import NoteForm
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64


def root_redirect(request):
    """
    Redirects the root URL to the login page.
    """
    return redirect('main')

def main(request):
    return render(request, 'diary/main.html')

@login_required
def menu(request):
    """
    Render the main menu page of the diary application.
    """
    return render(request, 'diary/menu.html')

@login_required
def search(request):
    """
    Search public notes by creation date.
    """
    query_date = request.GET.get('date')
    search_results = None
    if query_date:
        search_results = Note.objects.filter(created_at__date=query_date, is_public=True)
    random_quote = Quote.objects.order_by('?').first()
    top_post = Note.objects.filter(is_public=True).annotate(
        like_count=Count('likes')
    ).order_by('-like_count').first()
    context = {
        'results': search_results,
        'quote': random_quote,
        'top_post': top_post,
        'query_date': query_date
    }
    return render(request, 'diary/search.html', context)

@login_required
def add_note(request):
    """
    Create a new note for the authenticated user.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('my_notes')
    else:
        form = NoteForm()
    return render(request, 'diary/add_note.html', {'form': form})

@login_required
def my_notes(request):
    """
    Display all notes created by the current user.
    """
    user_notes = Note.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'diary/my_notes.html', {'notes': user_notes})

@login_required
def edit_note(request, pk):
    """
    Edit an existing note created by the current user.
    """
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('my_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'diary/edit_note.html', {'form': form, 'note': note})

@login_required
def statistics(request):
    """
    Display mood statistics for the current user.
    """
    user_notes = Note.objects.filter(author=request.user).values('mood__name', 'created_at__date')
    if not user_notes:
        return render(request, 'diary/statistics.html', {'error': 'Додайте нотатки, щоб побачити графік'})
    df = pd.DataFrame(list(user_notes))
    df = df.rename(columns={'mood__name': 'mood'})
    mood_counts = df['mood'].value_counts().to_dict()
    plt.switch_backend('Agg')
    plt.figure(figsize=(10, 5))
    df['mood'].value_counts().plot(kind='bar', color=['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b'])
    plt.title('Мій настрій за весь час')
    plt.ylabel('Кількість днів')
    plt.xticks(rotation=45)
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    return render(request, 'diary/statistics.html', {
        'mood_counts': mood_counts,
        'graph': graph
    })

@login_required
def notes_feed(request):
    """
    Display paginated feed of public notes.
    """
    notes_list = Note.objects.filter(is_public=True).order_by('-created_at')
    paginator = Paginator(notes_list, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'diary/notes.html', {'page_obj': page_obj})

@login_required
def songs_list(request):
    """
    Display paginated list of songs.
    """
    songs = Song.objects.all().order_by('-created_at')
    paginator = Paginator(songs, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'diary/songs.html', {'page_obj': page_obj})

@login_required
def note_detail(request, pk):
    """
    Display details of a single note.
    """
    note_item = get_object_or_404(Note, pk=pk)
    if not note_item.is_public and note_item.author != request.user:
        return redirect('notes_feed')
    return render(request, 'diary/note.html', {'note': note_item})
