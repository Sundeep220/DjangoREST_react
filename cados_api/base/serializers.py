from .models import Advocate,Company
from rest_framework.serializers import ModelSerializer,SerializerMethodField



class CompanySerializer(ModelSerializer):
    employees_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    def get_employees_count(self, obj): #starts witth get_   self refers to serializer and obj refers to model in this case Company
        count = obj.advocate_set.count()
        return count


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = ['username', 'bio', 'company','image']

