from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView, UpdateAPIView,DestroyAPIView,RetrieveAPIView

from . models import *
from . serializer import*

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

class PlansListCreate(ListCreateAPIView):
    queryset =Plan.objects.all()
    serializer_class = PlanSerilizer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PlanSerilizer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK )

    def create(self, request):
        serializer = PlanSerilizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PlanUpdatedelete(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    queryset =Plan.objects.all()
    serializer_class = PlanSerilizer


class ComapanyCrud(ModelViewSet):
    queryset= Company.objects.all()
    serializer_class = CompanySerilizer
 

from datetime import datetime, timedelta

class UserActivePlanes(ListCreateAPIView):
    queryset =UserPlans.objects.all()
    serializer_class = UserPlansSerializers

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        

        serializer = UserPlansSerializers(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK )

    def create(self, request):
        serializer = UserPlansSerializers(data= request.data)
        if  serializer.is_valid():
            obj =  serializer.save()
            print("This is Activet date ", obj.ActivePlan)
            plan = obj.plan.plantype
            print("This is plan type ======================================", plan)
            if plan == "YEARLY":
                PlanExpire =  obj.ActivePlan + timedelta(365)     
                obj.PlanExpire = PlanExpire
                obj.save()
            elif plan == "MONTHLY":
                PlanExpire =  obj.ActivePlan + timedelta(30)
                obj.PlanExpire = PlanExpire
                obj.save()
           
            return Response(serializer.data,status=status.HTTP_200_OK )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

      



#   def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             first_name = validated_data['first_name'],
#             last_name= validated_data['last_name'],
#             email = validated_data['email'],
#             password = make_password(validated_data['password']),
#             usertype = validated_data['usertype']
#             )
      
    
#         user.save()
#         return user










    # def get_email(self, obj):
    #     user_id = self.initial_data['userid']  # get the `userid` from the request body
    #     user = NewUser.objects.get(pk=user_id)  # fetch the user from DB
    #     return UserlistSerializer(instance=user).data

    





        
            
