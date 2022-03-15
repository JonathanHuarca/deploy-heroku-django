from rest_framework import routers
from .views import UserView

# router = routers.DefaultRouter()

# router.register('api/v1/profile', ProfileView.as_view())

# urlpatterns = router.urls 

from django.urls import path # add this

urlpatterns = [
    path('api/v1/user/<pk>', UserView.as_view()),  # Django admin route
]