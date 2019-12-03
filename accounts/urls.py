from django.urls import path
from .import views
#from polls import views

urlpatterns=[
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    #path('polls/',views.polls,name="polls"),
]