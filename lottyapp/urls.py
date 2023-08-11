from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('game/', views.lottery_entry, name='game'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
      path('upload-excel/', views.upload_excel, name='upload_excel'),
    
     

  
]

