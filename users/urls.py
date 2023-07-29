from django.urls import path
from .  import views
urlpatterns = [
    path('',views.homePage,name='home'),
    path('register/',views.register,name='register'),
    path('update_user/<str:pk>',views.updateUser,name='update_user'),
    path('delete_user/<str:pk>',views.deleteUser,name='delete_user'),
    path('login/',views.login,name='login'),
    path('about/',views.aboutPage,name='about'),
]