from rest_framework import serializers
from .models import WishList

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('uid', 'name', 'description', 'active', 'created_on', 'created_by',
                  'updated_on', 'updated_by',)
        read_only_fields = ('uid', 'created_by','updated_on', 'updated_by',)
