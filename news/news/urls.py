from django.urls import path

from . import views

urlpatterns = [
    path('readnews/', views.readnews, name='readnews'),
    path('writenews/',views.writenews, name='writenews')
]