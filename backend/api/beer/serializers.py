from rest_framework import serializers
from .models import Beer

class BeerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beer
        fields = ["id", "name", "name_kr", "style", "country", "abv"]