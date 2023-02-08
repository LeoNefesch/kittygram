from django.urls import include, path

from cats.views import APICat, APICatDetail

urlpatterns = [
   path('cats/', APICat.as_view(), name='cat_list'),
   path('cats/<int:id>/', APICatDetail.as_view(), name='cat_detail'),
]

