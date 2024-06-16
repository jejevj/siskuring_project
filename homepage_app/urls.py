from django.urls import path
from homepage_app.views import *
urlpatterns = [
    path('',homepage, name="home")
]
