from django.contrib import admin
from django.urls import path

from residential.views import appartment_list_view
from buildings.views import building_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appartments/', appartment_list_view),
    path('buildings/', building_list_view)
]
