from rest_framework import serializers
from .models import ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReviewModel
        fields = [
            "id",
            # "title",
            "rate",
            "content",
            "author",
            "beer",
            "beer_name",
            "created_date",
            "last_edit_date",
            "image_url"
        ]