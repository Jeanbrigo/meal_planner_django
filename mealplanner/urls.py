from django.contrib import admin
from knox import views as knox_views
from django.urls import path, include
from rest_framework import routers
from meals.views import MealViewSet, RegisterAPI, LoginAPI, ChangePasswordView

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'meals', MealViewSet) #register "/meals" routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
