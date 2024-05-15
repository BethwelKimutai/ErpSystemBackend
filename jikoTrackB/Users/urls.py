from django.urls import path
from .views import Register, Login,GetUser,Logout

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user', GetUser.as_view()),
    path('logout', Logout.as_view()),
]
