from . import views
from django.urls import path

urlpatterns = [
    path('' , views.home , name='home'),
    path('library' , views.library , name='library'),
    path('add' , views.add_game , name='add_game'),
    path("delete/<int:id>/", views.delete_game, name="delete"),
    path('details/<int:id>' , views.game_details , name='game_details'),
    path('edit/<int:id>' , views.edit_game , name='edit'),
    path('stats' , views.stats , name='stats')
]