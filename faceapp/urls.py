from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.test1,name='test'),
    path('fb',views.test2,name='fb')
]