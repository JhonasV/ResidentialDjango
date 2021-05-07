from django.shortcuts import render
from .models import Building
# Create your views here.


def building_list_view(request):
    buildings = Building.objects.all()
    context = {'buildings': buildings}
    return render(request, 'index.html', context)

def building_form_view(request):
    return

def building_delete_view(request):
    return