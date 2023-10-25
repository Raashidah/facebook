from django.urls import path,include
from . import views

urlpatterns = [
    
    path('/fb/',views.face,name='fb'),
    path('login/',views.log,name='login'),
    path('pass/',views.password,name='pass'),
    path('main/',views.home,name='main'),
    path('pro/',views.changeProfile,name='profile'),
    path('text/',views.test,name='test'),
    
]