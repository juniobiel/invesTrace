from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include

# Define the right template for host home
def home(request):
    return render(request, 'pages/base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('goals.urls'))
]
