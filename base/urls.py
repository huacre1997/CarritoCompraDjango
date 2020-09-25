from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from App.Controllers.IndexController import IndexController
from App.Controllers.ProductsController import ProductsController
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('login/',LoginFormView.as_view(),name="login")


]
