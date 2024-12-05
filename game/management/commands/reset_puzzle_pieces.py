from django.core.management.base import BaseCommand
from game.models import Level, PuzzlePiece
from game.utils import slice_and_save_puzzle_pieces


class Command(BaseCommand):
    help = 'Reset puzzle pieces for a specific level'

    def add_arguments(self, parser):
        parser.add_argument('level_id', type=int, help='level ID')
        parser.add_argument('image_path', type=str, help='Path to original image')
        parser.add_argument('output_dir', type=str, help='Directory for saving pieces')
        parser.add_argument('--rows', type=int, default=5, help='Number of split lines')
        parser.add_argument('--cols', type=int, default=5, help='Number of partition columns')

    def handle(self, *args, **options):
        level_id = options['level_id']
        image_path = options['image_path']
        output_dir = options['output_dir']
        rows = options['rows']
        cols = options['cols']

        try:
            level = Level.objects.get(id=level_id)
        except Level.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Level with id {level_id} does not exist."))
            return

        PuzzlePiece.objects.filter(level=level).delete()
        self.stdout.write(f"Old puzzle pieces for level {level_id} deleted.")

        pieces_data = slice_and_save_puzzle_pieces(level, image_path, output_dir, rows, cols)  # Передаём объект Level
        if not pieces_data:
            self.stdout.write(self.style.ERROR("Failed to slice and save puzzle pieces."))
            return

        PuzzlePiece.objects.bulk_create([PuzzlePiece(**piece) for piece in pieces_data])
        self.stdout.write(self.style.SUCCESS(f"Puzzle pieces for level {level_id} successfully reset."))
