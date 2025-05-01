from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

# Create your views here.

def get_members(request):  
    members = [
        {"name": "Rama", "age": 28, "specialty": "DataAn"},
        {"name": "Ahmad", "age": 23, "specialty": "ML"},
        {"name": "salma", "age": 24, "specialty": "AI"},
        {"name": "AbdAllah", "age": 22, "specialty": "Fullstack"},
        {"name": "hnadi", "age": 24, "specialty": "backend"},

    ]
    return JsonResponse(members, safe=False)
