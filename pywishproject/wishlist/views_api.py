from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import WishList
from .serializers import WishListSerializer

class WishListViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        assined_only = bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assined_only:
            queryset = queryset.filter(wishlist__isnull=False)
        return queryset.filter(created_by=self.request.user.username).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username)
