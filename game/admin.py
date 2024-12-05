from .models import Level, Puzzle, PuzzlePiece, UserInteraction, Game, GameLevel
from django.utils.html import format_html
from django.contrib import admin

admin.site.register(UserInteraction)
admin.site.register(Game)
admin.site.register(GameLevel)


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ['name', 'difficulty', 'created_at', 'image']
    search_fields = ['name', 'description']


class PuzzlePieceInline(admin.TabularInline):
    model = PuzzlePiece
    extra = 3
    fields = ['image_preview', 'position_x', 'position_y', 'is_solved']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" >')
        return "No Image"

    image_preview.short_description = 'Preview'


@admin.register(PuzzlePiece)
class PuzzlePieceAdmin(admin.ModelAdmin):
    list_display = ['level', 'image_preview', 'position_x', 'position_y', 'is_solved']
    search_fields = ['level__number', 'position_x', 'position_y']
    list_filter = ['level']
    autocomplete_fields = ['level']

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" >')
        return "No Image"

    image_preview.short_description = 'Preview'


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['number', 'correct_answer', 'is_solved', 'get_puzzle_pieces']
    search_fields = ['number', 'correct_answer']
    list_filter = ['is_solved']
    inlines = [PuzzlePieceInline]

    def get_puzzle_pieces(self, obj):
        return f"{obj.puzzle_pieces.count()} pieces"

    get_puzzle_pieces.short_description = 'Puzzle Pieces Count'
