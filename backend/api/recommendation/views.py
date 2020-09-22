from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
from beer.models import Beer
from beer.serializers import BeerSerializer
from api.settings import ALGO_PATH
# Create your views here.

@api_view(['GET'])
def svd(request):
    with open(ALGO_PATH, 'rb') as file:
        algo = pickle.load(file)
    candidate_beers = [1,3,4] # 안먹어본 beer_id 리스트

    predictions = [algo.predict("user_id가 들어갈 예정", beer_id) for beer_id in candidate_beers]

    # est로 부터 정렬하기 위한 함수
    def sortkey_est(p):
        return p.est

    # est 내림차순으로 정렬
    predictions.sort(key=sortkey_est, reverse=True)

    # 추천 리스트
    tops = predictions[:50]

    # 맥주 pk 뽑기
    pk_list = []
    for uid,iid,r,est,k in tops:
        pk_list.append(iid)
    # 추천 맥주 가져와서 보내기
    beers = Beer.objects.filter(pk__in=pk_list)
    serializer = BeerSerializer(beers, many=True)
    return Response(serializer.data)