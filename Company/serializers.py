from rest_framework import serializers
from  .models import Company_data,Employee


class companySerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company_data
        fields='__all__'


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'