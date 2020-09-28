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
            "created_date",
            "last_edit_date"
        ]