from django.urls import path
from .views import get_items, create_item

urlpatterns = [
    path("api/items/", get_items, name="get_items"),
    path("api/items/", create_item, name="create_item")
]
