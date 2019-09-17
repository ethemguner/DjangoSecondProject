from django.urls import path
from users.views import user_register, user_login, user_logout, update_information

urlpatterns = [
    path('register/', user_register, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('myProfile/<slug:username>', update_information, name='user-settings'),
]
