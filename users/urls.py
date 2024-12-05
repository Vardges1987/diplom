from django.urls import path
from . import api_views
from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('', user_views.home, name='home'),
    path('login/', user_views.user_login, name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/<int:level_id>/', user_views.profile, name='profile'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('logout/', user_views.logout, name='logout'),

    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', api_views.UserDetailView.as_view(), name='user-detail'),
    path('user-profiles/<int:pk>/', api_views.UserProfileDetailView.as_view(), name='user-profile-detail'),
]

