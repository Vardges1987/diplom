from django.contrib import admin
from .models import UserProfile
from .models import UserProgress


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'level_id']
    search_fields = ['user__username']

    def __str__(self):
        return f"Progress of {self.user.username} - Level {self.level_id}"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'completed_levels_count']
    search_fields = ['user__username']

    def completed_levels_count(self, obj):
        return obj.completed_levels.count()

    completed_levels_count.short_description = 'Completed Levels Count'
