from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:blog_id>', detail, name ="detail"),
    path('new/', new, name = "new"),
    path('edit/<str:blog_id>', edit, name = "edit"),
    path('delete/<str:blog_id>', delete, name = "delete"),
    path('like/', post_likes, name="post_likes"),
    path('map/', dramamap, name="map"),
    path('map1/', dramamap1, name="map1"),
    path('map2/', dramamap2, name="map2"),
    path('map3/', dramamap3, name="map3"),
    path('map4/', dramamap4, name="map4"),
    path('map5/', dramamap5, name="map5"),
]