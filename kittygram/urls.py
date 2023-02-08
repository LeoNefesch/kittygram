from django.urls import include, path

from cats.views import cat_detail, cat_list, hello

urlpatterns = [
   path('cats/', cat_list, name='cat_list'),
   path('cats/<int:id>/', cat_detail, name='cat_detail'),
   path('hello/', hello, name='hello'),
]

