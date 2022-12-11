from django.contrib import admin
from django.urls import path,include
from . views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("company",ComapanyCrud, basename="com")
urlpatterns = [

    path('all',include(router.urls)),
    path('plans',PlansListCreate.as_view()),
    path('plans/<pk>',PlanUpdatedelete.as_view()),
    path('buyplan/',UserActivePlanes.as_view()),

]