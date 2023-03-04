from .models import Meal
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our MealSerializer
class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Meal
        # the fields that should be included in the serialized output
        fields = ['id', 'name', 'imageURL', 'dayToEat','ingredients' ]