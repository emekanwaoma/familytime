from django.urls import path
from users.views import RegisterUser, LoginUser

urlpatterns = [
    path('signup/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
]