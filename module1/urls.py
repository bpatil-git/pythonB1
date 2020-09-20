
from django.urls import path
from . import views

app_name = 'module1'
urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('travel-oper/', views.travel_oper, name="travel_oper"),
    path('learnings/', views.learnings, name="learnings"),

]
