from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import companySerializer,EmployeeSerializers
# Create your views here.
from Company.models import Company_data,Employee
from rest_framework.decorators import action

class CompanyViewset(viewsets.ModelViewSet):
       queryset=Company_data.objects.all()
       serializer_class=companySerializer
       
       @action(detail=True,methods=['get'])
       def employees(self,request,pk=None):
           try:
             company=Company_data.objects.get(pk=pk)
             emps=Employee.objects.filter(company=company)
             emps_serializers=EmployeeSerializers(emps,many=True,context={'request':request})
             return Response(emps_serializers.data)
           except Exception as DoesnotExist:
              print(DoesnotExist)
              return Response("Company doesn't exist")

class  EmployeeViewset(viewsets.ModelViewSet):
       queryset=Employee.objects.all()
       serializer_class=EmployeeSerializers     