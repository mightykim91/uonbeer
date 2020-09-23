from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createReview), #리뷰 생성
    path('<int:review_id>/edit/', views.editReview), #리뷰 수정
    path('<int:review_id>/delete/', views.deleteReview), #리뷰 삭제
    path('all/', views.getAllReview), #전체 리뷰 출력
    path('<int:review_id>/', views.getReview), #review_id에 해당하는 리뷰 출력
]