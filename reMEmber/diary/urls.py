"""
URL configuration for the diary application.
"""


from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('notes/', views.notes_feed, name='notes'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('my-notes/', views.my_notes, name='my_notes'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('add/', views.add_note, name='add_note'),
    path('search/', views.search, name='search'),
    path('statistics/', views.statistics, name='statistics'),
    path('songs/', views.songs_list, name='songs'),
    path('menu/', views.menu, name='menu'),
]
