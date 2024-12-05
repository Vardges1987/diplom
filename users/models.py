from django.db import models
from django.contrib.auth.models import User
from game.models import Level


#

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    score = models.IntegerField(default=0)
    completed_levels = models.ManyToManyField(Level, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_id = models.IntegerField(default=1)
    current_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    completed_levels = models.ManyToManyField('game.GameLevel', blank=True)

    def __str__(self):
        return f"Progress of {self.user.username} - Level {self.level_id}"

    def is_level_completed(self, level):
        return level in self.completed_levels.all()
