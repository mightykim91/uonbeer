from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import ReviewModel
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getAllReview(request):
    reviews = ReviewModel.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def getReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=200)


@api_view(["POST"])
def createReview(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=200)
        
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def editReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    if review.author != request.user:
        return Response({"message":"작성자만 글을 수정할 수 있습니다"})

    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
    return Response(serializer.errors)


@api_view(["DELETE"])
def deleteReview(request, review_id):
    review = get_object_or_404(ReviewModel, pk=review_id)
    if review.author == request.user:
        review.delete()
        return Response(
            {
                "status":"success",
                "message":"리뷰가 성공적으로 삭제되었습니다."
            })

    else:
        return Response({
            "status":"failed",
            "message":"리뷰 작성자만 삭제가 가능합니다."
        })
    