from django.urls import path
from . import views 

urlpatterns =[
    path('computer/', views.ComputerListCreate.as_view(), name ='computers'),
    path('computer_create/', views.ComputerListCreate.as_view(), name='computer_create'),
    path('computer/<int:id>', views.ComputerViewUpdateDelete.as_view(), name='computer'),
    path('computer_update/<uuid:pk>/', views.ComputerViewUpdateDelete.as_view(), name='computer_update'),
    path('computer_delete/<uuid:pk>/', views.ComputerViewUpdateDelete.as_view(), name='computer_delete'),
    path('player/', views.PlayerListCreate.as_view(), name ='computers'),
    path('player_create/', views.PlayerListCreate.as_view(), name='computer_create'),
    path('player/<int:id>', views.PlayerViewUpdateDelete.as_view(), name='computer'),
    path('player_update/<uuid:pk>/', views.PlayerViewUpdateDelete.as_view(), name='computer_update'),
    path('player_delete/<uuid:pk>/', views.PlayerViewUpdateDelete.as_view(), name='computer_delete'),
]