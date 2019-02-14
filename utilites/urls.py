from django.urls import path
from . import views  # 현재폴더의 views 불러옴 


urlpatterns = [
    path('', views.index, name='index'),
    ]