# from django.urls import path
# from .views import ProductList

# urlpatterns = [
#     path("", ProductList.as_view(), name="product-list"),
# ]


from rest_framework.routers import DefaultRouter

from .views import ProductViewSet


router = DefaultRouter()
router.register("", ProductViewSet, basename="product")

urlpatterns = router.urls