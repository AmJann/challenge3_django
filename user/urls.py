from django.urls import path
from . import views  

urlpatterns =[
    path('user_create/', views.CreateUser.as_view(), name='user_create'),
    path('users/<name>', views.CheckUser.as_view(), name ='users'),
    path('add-score/', views.addScore.as_view(), name='add_score'),
    path('top-score/', views.TopScoresView.as_view(), name='top_score'),
    path('top-score-game/', views.getScorebyGameId.as_view(), name='score_by_game_id'),
]


