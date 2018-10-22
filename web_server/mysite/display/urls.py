from django.urls import path

from . import views

app_name = 'display'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:id>', views.findByID, name='findByID'),
]