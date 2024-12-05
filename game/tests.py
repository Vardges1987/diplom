from django.test import TestCase
from django.contrib.auth.models import User
from .models import Level, Puzzle, Game, PuzzlePiece, UserInteraction
from datetime import timedelta


class LevelModelTest(TestCase):

    def setUp(self):
        self.level = Level.objects.create(
            number=1,
            correct_answer="Answer",
            description="Description of level 1",
            piece_width=100,
            piece_height=100
        )

    def test_level_creation(self):
        level = self.level
        self.assertEqual(level.number, 1)
        self.assertEqual(level.correct_answer, "Answer")
        self.assertEqual(level.description, "Description of level 1")
        self.assertEqual(level.piece_width, 100)
        self.assertEqual(level.piece_height, 100)
        self.assertFalse(level.is_solved)

    def test_str_method(self):
        self.assertEqual(str(self.level), "Level 1")


class PuzzleModelTest(TestCase):

    def setUp(self):
        self.level = Level.objects.create(number=1)
        self.puzzle = Puzzle.objects.create(
            level=self.level.number,
            name="Puzzle 1",
            correct_answer="Correct Answer",
            difficulty="Easy",
            description="Puzzle description"
        )

    def test_puzzle_creation(self):
        puzzle = self.puzzle
        self.assertEqual(puzzle.level, self.level.number)
        self.assertEqual(puzzle.name, "Puzzle 1")
        self.assertEqual(puzzle.correct_answer, "Correct Answer")
        self.assertEqual(puzzle.difficulty, "Easy")
        self.assertEqual(puzzle.description, "Puzzle description")

    def test_str_method(self):
        self.assertEqual(str(self.puzzle), "Puzzle 1")


class GameModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.game = Game.objects.create(user=self.user, level=1)

    def test_game_creation(self):
        game = self.game
        self.assertEqual(game.user.username, "testuser")
        self.assertEqual(game.level, 1)

    def test_str_method(self):
        self.assertEqual(str(self.game), "testuser")


class PuzzlePieceModelTest(TestCase):

    def setUp(self):
        self.level = Level.objects.create(number=1)
        self.piece = PuzzlePiece.objects.create(
            level=self.level,
            position_x=10,
            position_y=20,
            is_solved=False
        )

    def test_puzzle_piece_creation(self):
        piece = self.piece
        self.assertEqual(piece.level, self.level)
        self.assertEqual(piece.position_x, 10)
        self.assertEqual(piece.position_y, 20)
        self.assertFalse(piece.is_solved)

    def test_str_method(self):
        self.assertEqual(str(self.piece), "Piece (10, 20) of Level 1")


class UserInteractionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.puzzle = Puzzle.objects.create(name="Puzzle 1", level=1, correct_answer="Correct",
                                            description="Description")
        self.interaction = UserInteraction.objects.create(
            user=self.user,
            puzzle=self.puzzle,
            success=True
        )

    def test_user_interaction_creation(self):
        interaction = self.interaction
        self.assertEqual(interaction.user.username, "testuser")
        self.assertEqual(interaction.puzzle.name, "Puzzle 1")
        self.assertTrue(interaction.success)

    def test_duration_method(self):
        self.interaction.end_time = self.interaction.start_time + timedelta(seconds=5)
        self.assertEqual(self.interaction.duration(), 5.0)

    def test_duration_method_no_end_time(self):
        self.assertIsNone(self.interaction.duration())
