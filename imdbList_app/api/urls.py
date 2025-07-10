from django.urls import path, include
from rest_framework.routers import DefaultRouter
from imdbList_app.api.views import (WatchListAV, WatchDetailAV,
                                    StreamPlatformAV, StreamPlatformDetailAV,
                                    ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename = 'streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='watch-detail'),
    
    path('', include(router.urls)),
    
    # path('stream/',StreamPlatformAV.as_view(), name='streamplatform-list'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create', ReviewCreate.as_view() , name = 'review-create'), 
    path('<int:pk>/reviews', ReviewList.as_view() , name = 'review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
]