from django.urls import path, include
from users import views as user_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('profile/', user_views.profile, name='profile'),
    path('game/', include('game.urls')),
    path('users/', include('users.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('logout/', user_views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
