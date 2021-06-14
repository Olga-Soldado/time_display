from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('time_display', views.time_display)
]
