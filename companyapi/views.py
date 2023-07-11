
from django.http import HttpResponse,JsonResponse

from django.shortcuts import render
from api.models import Company
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import CompanySerializer

def home(request):
    return render(request, 'index.html')

from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = []

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []

@api_view(['GET'])
def api_response(request):
    # Fetch the API data
    companies = Company.objects.all()  # Example query, modify as per your needs

    # Serialize the data
    serializer = CompanySerializer(companies, many=True)

    # Return the serialized data as API response
    return Response(serializer.data)
