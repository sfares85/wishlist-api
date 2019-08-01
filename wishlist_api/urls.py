from django.contrib import admin
from django.urls import path
from items import views
from API.views import ItemListView, ItemDetailView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('items/list/', views.item_list, name='item-list'),
	path('items/API/list/', ItemListView.as_view(), name='API-list'),
	path('items/detail/<int:item_id>/', views.item_detail, name='item-detail'),
	path('items/API/detail/<int:item_id>/', ItemDetailView.as_view(), name='API-detail'),
	path('items/wishlist/', views.wishlist, name='wishlist' ),
	path('user/register/', views.user_register, name='user-register'),
	path('user/login/', views.user_login, name='user-login'),
	path('user/logout/', views.user_logout, name='user-logout'),
	path('API/user/login/', TokenObtainPairView.as_view(), name='API-user-login'),
	path('items/<int:item_id>/favorite/', views.item_favorite, name='item-favorite'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)