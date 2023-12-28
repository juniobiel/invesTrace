from . import views
from django.urls import path

urlpatterns = [
    path('goals/', views.home),
    path('goal/<int:id>', views.goals),
]