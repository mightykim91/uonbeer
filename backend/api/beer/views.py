from django.shortcuts import render, get_object_or_404
from django.db.models import F, Func, Value, Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Beer

from .serializers import BeerSerializer
# Create your views here.

#Return all beers
@api_view(['GET'])
def getAllBeer(request):
    beers = Beer.objects.all()
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)


#Get specified beer information
@api_view(['GET'])
def getSingleBeer(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    serializer = BeerSerializer(beer)
    return Response(serializer.data)


#API to add new beer
@api_view(['POST'])
def addNewBeer(request):
    beer_serializer = BeerSerializer(data=request.data)
    if beer_serializer.is_valid():
        beer_serializer.save()
        return Response(request.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


#API to edit beer information
@api_view(['PUT'])
def editBeerInfo(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    serializer = BeerSerializer(beer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
    # return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.error)


#API to delete specified beer
@api_view(['DELETE'])
def deleteBeer(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id) #Return 404 if beer doesn't exist
    beer.delete()
    return Response(status.HTTP_200_OK)
    

#API to search beers
@api_view(['GET'])
def searchBeer(request):
    #Get keyword from query string
    keyword = request.GET.get('keyword').replace(" ", "")
    #Get all beer
    beer = Beer.objects.all()
    #Create nospace column and add beer name after removing all spaces
    preprocess = beer.annotate(
        nospace1=Func( F('name_kr'), Value(" "), Value(""), function="replace" ), 
        nospace2=Func( F('name'), Value(" "), Value(""), function="replace"),
        )
    #Search beer for keyword 
    rst = preprocess.filter(Q(nospace1__contains=keyword) | Q(nospace2__contains=keyword))
    serializer = BeerSerializer(rst, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({"message": "찾으시는 맥주가 없습니다 ㅠㅠ"}, status=204)
    
    return Response(status=400)
