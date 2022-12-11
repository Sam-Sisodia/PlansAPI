from  rest_framework import serializers

from . models import *



# class PlanSerilizer(serializers.ModelSerializer):
#     Company_details = serializers.SerializerMethodField(method_name='company_name')
#     class Meta:
#         model = Plan
#         fields = ['id','name','price','create_at','update_at','Company',"Company_details"]

#     def company_name(self, ownerObj):
#         queryset = Company.objects.all()
#         return PlanSerilizer(queryset, many=True).data



    
    # def get_booking(self, obj):
    #     booking = BookingSerializer(obj.hall_owner.all(),many=True).data
    #     return booking
class PlanSerilizer(serializers.ModelSerializer):
    Company_name = serializers.CharField(read_only =True,source='Company.name',default="Company_not_Assiggn")
    class Meta:
        model = Plan
        fields = ['id','name','price','create_at','update_at','plantype','Company','Company_name']

    

class CompanySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class UserPlansSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPlans
        fields = ['ActivePlan','PlanExpire','user','plan']
        read_only_fields = ['PlanExpire']