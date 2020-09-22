from django.test import TestCase
from .models import ReviewModel
from django.conf import settings

# Create your tests here.
class ModelTest(TestCase):
    def modelCreationTest(self):
        model = ReviewModel(
            title = "test",
            content = "test",
            author = settings.AUTH_USER_MODEL
        )