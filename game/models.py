from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    number = models.IntegerField(unique=True)
    correct_answer = models.CharField(max_length=255)
    description = models.TextField(default="Default description")
    piece_width = models.IntegerField(default=100)
    piece_height = models.IntegerField(default=100)
    image = models.ImageField(upload_to='puzzle_pieces/', null=False, default='puzzle_pieces/default_image.png')
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return f"Level {self.number}"


class Puzzle(models.Model):
    level = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=200, null=True)
    difficulty = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='puzzle_pieces/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Game(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username


class GameLevel(models.Model):
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField(default=1)
    description = models.TextField()

    def __str__(self):
        return f"Level {self.id} - {self.title}"


def puzzle_piece_upload_path(instance, filename):
    level_number = instance.level.number
    return f"puzzle_pieces{level_number}/{filename}"


class PuzzlePiece(models.Model):
    level = models.ForeignKey('Level', related_name='puzzle_pieces', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='puzzle_piece/')
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return f"Piece ({self.position_x}, {self.position_y}) of Level {self.level.number}"


class PuzzleQuestion(models.Model):
    levels = models.ManyToManyField('Level', related_name='questions')
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Question: {self.question.level.name}"


class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    success = models.BooleanField(default=False)

    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return None
