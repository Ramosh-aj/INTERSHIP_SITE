from django.urls import path  
from .views import get_members  

urlpatterns = [
       path('members/', get_members), 
]


