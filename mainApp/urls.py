from django.urls import path
from . import views

urlpatterns = [
      # Path Converters
      # int: numbers
      # str: strings
      # path: whole urls /
      # slug: hyphen-and_underscores_stuff
      # UUID: universally unique identifier

      path('', views.home, name="home"),
      path('create_box', views.create_box, name="create-box"),
      path('box_list', views.box_list, name="box-list"),
]