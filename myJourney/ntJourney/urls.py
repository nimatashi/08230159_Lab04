from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),            # Home page
    path('about/', views.aboutMe, name='aboutMe'),  # About Me page
]
