from django.urls import path, include
from rest_framework import routers

from . import views
from . import views_api


router = routers.DefaultRouter()
router.register(r'wishs', views_api.WishListViewSet)

urlpatterns = [
    path('wishlists', views.index, name='index'),
    path('api/v1/wishlists/', views_api.WishListViewSet.as_view({'get': 'list'}), name='api-list'),
    path('api/v2/', include(router.urls)),
]
