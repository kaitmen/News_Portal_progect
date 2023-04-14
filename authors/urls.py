
from django.urls import path
from .views import *
app_name = "authors"
urlpatterns = [

   path('', PostsList.as_view()),
   path('search/', PostsSearch.as_view()),

   path('<int:pk>', PostDetail.as_view(), name = "post"),
]