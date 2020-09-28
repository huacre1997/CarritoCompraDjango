from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from App.Controllers.IndexController import *
from django.conf.urls.static import static
from .views import LogoutView,LoginFormView

urlpatterns = [
    path('', IndexController.index, name="index"),
    path('login/',LoginFormView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="/"),name="logout")

]
