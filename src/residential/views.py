from django.shortcuts import render
from .models import Appartment

# Create your views here.

def appartment_list_view(request):
    appartments = Appartment.objects.all()
    context = { 'appartments': appartments }
    return render(request, 'appartments/index.html', context)