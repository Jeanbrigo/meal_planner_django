from .models import Meal
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Meal.objects.all()
    # The serializer class for serializing output
    serializer_class = MealSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]