from django.urls import path

from . import views
from . import views_api

urlpatterns = [
    path('wishlists', views.index, name='index'),
    path('api/wishlists/', views_api.WishListViewSet.as_view({'get': 'list'}), name='api-list'),
]
