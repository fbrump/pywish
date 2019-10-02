from rest_framework import serializers
from .models import WishList

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('id', 'name', 'description', 'active', 'created_on', 'created_by',
                  'updated_on', 'updated_by',)
        read_only_fields = ('id', 'created_on', 'created_by','updated_on', 'updated_by',)
