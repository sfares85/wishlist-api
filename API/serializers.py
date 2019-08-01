from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name']

class ItemSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "API-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
	added_by = UserSerializer()
	favorite = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['name','detail','added_by','favorite']

	def get_favorite(self,obj):
		return obj.favs.count()

class FavoriteItemSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = FavoriteItem
		fields = ['user','id']

class ItemDetailSerializer(serializers.ModelSerializer):
	favs = FavoriteItemSerializer(many=True)
	class Meta:
		model = Item
		fields = '__all__'


