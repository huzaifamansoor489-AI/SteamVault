from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Game


def home(request):
  games = Game.objects.all()
  context = {
    "total_games" : Game.objects.count(),
    "playing" : Game.objects.filter(status = "playing").count(),
    "completed" : Game.objects.filter(status = "completed").count(),
    "wishlist" : Game.objects.filter(status = "wishlist").count(),
    "featured_games" : games[:3],

  }
  return render(request , 'home.html' , context)
def library(request):
  games = Game.objects.all()
  return render(request , 'library.html' , {"games":games})
def add_game(request):
   if request.method == "POST":
    game_name = request.POST.get("game_name")
    game_genre = request.POST.get("game_genre")
    game_platform = request.POST.get("game_platform")
    game_developer = request.POST.get("game_developer")
    release_year = request.POST.get("release_year")
    hours_played = request.POST.get("hours_played")
    game_description = request.POST.get("game_description")
    status = request.POST.get('status')
    rating = request.POST.get('rating')

    Game.objects.create(
      game_name = game_name,
      game_genre = game_genre,
      game_platform = game_platform,
      game_developer =game_developer,
      release_year = release_year,
      hours_played = hours_played,
      game_description = game_description,
      status = status,
      rating =rating
    )
    
    return redirect('library')
   return render(request , 'add.html')  
def game_details(request , id):
    game = Game.objects.get(id=id)

    return render(
        request,
        "detail.html",
        {"game": game}
    )
def delete_game(request,id):
      game = Game.objects.get(id=id)
      game.delete()

      return redirect("library")

def edit_game(request ,id):
    game = Game.objects.get(id=id)
    if request.method == "POST":
        game.game_name = request.POST.get("game_name")
        game.game_genre = request.POST.get("game_genre")
        game.game_platform = request.POST.get("game_platform")
        game.game_developer = request.POST.get("game_developer")
        game.release_year = request.POST.get("release_year")
        game.hours_played = request.POST.get("hours_played")
        game.game_description = request.POST.get("game_description")
        game.status = request.POST.get('status')
        game.rating = request.POST.get('rating')

        game.save()
        return redirect("game_details" , id =game.id)

    return render(request , 'add.html' ,{"game":game})
def stats(request):
  return render(request , 'stats.html')