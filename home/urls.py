from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name="home"),
    
    path("add",views.add,name='add'),
    path("update/<int:grocerylist_id>/",views.update),
    path("newlist",views.newlist),
    path("signin",views.signin,name='SignUp'),
    path("signup",views.signup,name='signIn'),
]
