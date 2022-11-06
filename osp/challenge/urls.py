from django.urls import path, include

from challenge import views

app_name = 'challenge'

urlpatterns = [
    path('', views.challenge_list_view, name='Challenge'),
    path('check/', views.challenge_acheive_update, name='ChallengeCheck'),
    path('forbidden/',views.forbidden_page, name='forbbiden' )
]