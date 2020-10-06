from django.shortcuts import render, get_object_or_404
from django.db.models import F, Func, Value, Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Beer

from .serializers import BeerSerializer

from .firebase import getURL
# Create your views here.

#Return all beers
@api_view(['GET'])
def getAllBeer(request):
    beers = Beer.objects.all()

    #데이터 전부다 들어오면 해제
    # for beer in beers:
    #     beer.image_url = getURL(beer.image_file_name)
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)


#Get specified beer information
@api_view(['GET'])
def getSingleBeer(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    beer.image_url = getURL(beer.image_file_name)
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
    style = request.GET.get('style')
    country = request.GET.get('country')
    abvmax = request.GET.get('abvmax')
    abvmin = request.GET.get('abvmin')
    #Get all beer
    beer = Beer.objects.all()
    #Create nospace column and add beer name after removing all spaces
    preprocess = beer.annotate(
        nospace1=Func( F('name_kr'), Value(" "), Value(""), function="replace" ), 
        nospace2=Func( F('name'), Value(" "), Value(""), function="replace"),
        lowercase=Func( F('name'), function="lower")
        )
    #Search beer for keyword, country, style, abv range
    rst = preprocess.filter((Q(nospace1__contains=keyword) | Q(nospace2__contains=keyword) | Q(lowercase__contains=keyword))&Q(abv__gte=abvmin)&Q(abv__lte=abvmax))
    if style == 'Etc':
        rst = rst.exclude(Q(style='Lager') | Q(style='Ale'))
    elif style != 'All':
        rst = rst.filter(style=style)
        print(rst)
    
    if country == 'Etc':
        rst = rst.exclude(country = 'KR')
    elif country != 'All':
        rst = rst.filter(country = country)

    serializer = BeerSerializer(rst, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({"message": "찾으시는 맥주가 없습니다 ㅠㅠ"}, status=204)
    
    return Response(status=400)
