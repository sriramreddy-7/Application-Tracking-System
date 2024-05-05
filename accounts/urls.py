from django.urls import path, include
from accounts import views


app_name = "accounts"



urlpatterns = [
    path("login_user/",views.login_user, name="login_user"),
    path("register/",views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
]