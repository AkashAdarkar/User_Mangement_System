from django.urls import path
from .  import views
urlpatterns = [
    path('',views.homePage),
    path('register/',views.register),
    path('login/',views.login),
    path('about/',views.aboutPage),
]