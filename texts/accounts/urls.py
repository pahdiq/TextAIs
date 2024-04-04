from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('home/', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('prices/', views.prices, name='prices'),
]
