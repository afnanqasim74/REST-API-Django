from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers
"""
router= routers.DefaultRouter()
router.register(r'companies', CompanyViewSet,basename='company')
router.register(r'employees', EmployeeViewSet,basename='employee')

urlpatterns = [    
    path('',include(router.urls))
      
]
"""
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', CompanyViewSet)

urlpatterns = [
    # ... other URL patterns ...
    path('api/v1/', include(router.urls)),
]
#companies/{companyId}/employees