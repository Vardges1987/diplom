from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Level, PuzzlePiece, PuzzleQuestion
from .forms import PuzzleAnswerForm
import random
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Game
from .serializers import GameSerializer


class GameListView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def level_list(request):
    levels = Level.objects.all()
    return render(request, 'game/level_list.html', {'levels': levels})


def next_level(request, level_number):
    level = get_object_or_404(Level, number=level_number)

    if not level.is_solved:
        return redirect('game:puzzle_view', level_id=level.id)

    next_level = Level.objects.filter(number=level.number + 1).first()

    if next_level:
        return redirect('game:puzzle_view', level_id=next_level.id)
    else:
        return redirect('game:puzzle_completed')


def puzzle_view(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    puzzle_pieces = list(level.puzzle_pieces.all())
    random.shuffle(puzzle_pieces)

    puzzle_area_width = 550
    puzzle_area_height = 550
    total_pieces = len(puzzle_pieces)
    rows = int(total_pieces ** 0.5)
    cols = rows if rows * rows == total_pieces else rows + 1
    piece_width = puzzle_area_width // cols
    piece_height = puzzle_area_height // rows

    if request.method == "POST":
        form = PuzzleAnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer.lower() == level.correct_answer.lower():
                next_level = Level.objects.filter(number=level.number + 1).first()
                return redirect('game:puzzle_view', level_id=next_level.id) if next_level else redirect(
                    'game:puzzle_completed')
            else:
                messages.error(request, "Incorrect answer, please try again.")
    else:
        form = PuzzleAnswerForm()

    context = {
        'level_id': level_id,
        'puzzle_pieces': puzzle_pieces,
        'form': form,
        'piece_width': piece_width,
        'piece_height': piece_height,
        'columns': cols,
        'rows': rows,
        'puzzle_area_width': puzzle_area_width,
        'puzzle_area_height': puzzle_area_height,
    }

    return render(request, 'game/puzzle.html', context)


# @login_required(login_url='/')
def puzzle_solved(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    next_level = Level.objects.filter(number=level.number + 1).first()
    if next_level:
        next_level_number = next_level.number
    else:
        next_level_number = None

    level_descriptions = {
        1: (
            "This amazing cathedral, "
            "the center of the Holy See and the symbol of the entire Catholic world, is astounding. "
            "Its walls and vaults remember many historical events. "
            "In its halls, you can see works of art by Michelangelo and Bernini."
        ),
        2: (
            "The Cathedral of the Immaculate Conception of the Blessed Virgin Mary "
            " is a neo-Gothic cathedral in Moscow , the largest Catholic cathedral in Russia ,"
            " the cathedral of the Archdiocese of the Mother of God , headed by Archbishop Metropolitan Paul Pezzi ."
            " The third Moscow Catholic church built before the 1917 Revolution , one of three currently operating"
            " Catholic churches in Moscow along with the Church of St. Louis and the Church of St. Olga .",
        ),
        3: "Masjid al-Haram (Arabic: ٱَلْمَسْجِدُ ٱلْحَرَا, romanized: al-Masjid al-Ḥarām,'The Sacred Mosque'),"
           "also known as the Sacred Mosque or the Great Mosque of Mecca,"
           " is considered to be the most significant mosque in Islam."
           " It encloses the vicinity of the Kaaba in Mecca, in the Mecca Province of Saudi Arabia",
    }
    description = level_descriptions.get(level.number, f"You've solved the puzzle for level {level.number}!")

    background_image = f"images/Level_{level.id}.png"

    return render(request, 'game/puzzle_solved.html', {
        'level': level,
        'description': description,
        'next_level': next_level,
        'background_image': background_image
    })


@login_required(login_url='/')
def check_puzzle(request, level_id):
    level = get_object_or_404(Level, id=level_id)

    if all(piece.is_solved for piece in PuzzlePiece.objects.filter(level=level)):
        return redirect('game:check_answer', level_number=level.number)
    return render(request, 'game/puzzle_incorrect.html', {'level': level})


@login_required
def check_answer(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    question = get_object_or_404(PuzzleQuestion, level=level)

    if request.method == 'POST':
        user_answer = request.POST.get("answer")
        if user_answer.strip().lower() == question.correct_answer.lower():
            level.is_solved = True
            level.save()
            return redirect('game:puzzle_solved', level_id=level.id)
        else:
            return render(request, 'game/puzzle_incorrect.html', {'level': level})

    return render(request, 'game/question.html', {'question': question, 'level': level})


def puzzle_question(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    background_image = f"images/Level_{level.id}.png"

    if request.method == 'POST':
        user_answer = request.POST.get("answer")
        if user_answer and user_answer.strip().lower() == level.correct_answer.lower():
            return redirect('game:puzzle_solved', level_id=level.id)
        else:
            return redirect('game:puzzle_incorrect', level_id=level.id)

    return render(request, 'game/puzzle_question.html',
                  {'level': level, 'background_image': background_image})


@login_required
def puzzle_incorrect(request, level_id):
    level = get_object_or_404(Level, id=level_id)

    background_image = f"images/Level_{level.id}.png"

    return render(request, 'game/puzzle_incorrect.html', {'level': level, 'background_image': background_image})


def home(request):
    context = {
        'welcome': 'Welcome to the game!',
    }
    return render(request, 'home.html', context)


def puzzle_completed(request):
    return render(request, 'game/puzzle_completed.html')
