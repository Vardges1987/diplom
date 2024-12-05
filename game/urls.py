from . import api_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('levels/', views.level_list, name='level_list'),
    path('puzzle/<int:level_id>/', views.puzzle_view, name='puzzle_view'),
    path('puzzle/<int:level_id>/question/', views.puzzle_question, name='puzzle_question'),
    path('puzzle/<int:level_id>/check/', views.check_puzzle, name='check_puzzle'),
    path('check-answer/<int:level_id>/', views.check_answer, name='check_answer'),
    path('puzzle/<int:level>/next/', views.next_level, name='next_level'),
    path('puzzle_solved/<int:level_id>/', views.puzzle_solved, name='puzzle_solved'),
    path('puzzle_incorrect/<int:level_id>/', views.puzzle_incorrect, name='puzzle_incorrect'),
    path('next_level/<int:level_number>/', views.next_level, name='next_level'),
    path('puzzle_completed/', views.puzzle_completed, name='puzzle_completed'),


    path('api/games/', api_views.GameListView.as_view(), name='game-list'),
    path('api/games/<int:pk>/', api_views.GameDetailView.as_view(), name='game-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
