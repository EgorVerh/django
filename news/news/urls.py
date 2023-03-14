from django.urls import path

from . import views

urlpatterns = [
    path('readnews/', views.ReadNewsView.as_view(), name='readnews'),
    path('writenews/',views.writenews, name='writenews'),
    path('changenews/<int:pk>',views.ChangeNewsView.as_view(),name='changenews'),
    path('readnews/<int:pk>',views.ConcretNewsView.as_view(),name='concretnews'),
]