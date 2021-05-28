from django.db.models.base import Model
from django.urls import path
from .views import ListTimeUuid, createTimeView

urlpatterns = [
    path('', ListTimeUuid.as_view(), name= 'key_value'), 
    path('list/', createTimeView, name='create')

]